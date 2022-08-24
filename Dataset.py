from __future__ import division
import numpy as np
from tslearn.datasets import UCR_UEA_datasets

ACCEPTED_DATASETS: list = []


class DataSet:
    def __init__(self, name: str, shape, distribution: list[int]) -> None:
        self.name = name
        self.shape = shape
        self.distribution = distribution

    def possiblePoolSizes(self) -> list[int]:
        allDivisors: list[int] = []
        numberOfTimeSteps = self.shape[1]
        for i in range(2, numberOfTimeSteps // 2 + 1):
            if numberOfTimeSteps % i == 0:
                allDivisors.append(i)
        return allDivisors

    def addToFinalList(self):  # Sorts the list based on the number of observations
        for i in range(len(ACCEPTED_DATASETS)):
            if self.shape[0] > ACCEPTED_DATASETS[i].shape[0]:
                ACCEPTED_DATASETS.insert(i, self)
                return
        ACCEPTED_DATASETS.append(self)

    def distributionToString(self) -> str:
        CLUSTERS_CNT: int = len(self.distribution)
        result: str = ''
        for i in range(CLUSTERS_CNT):
            result += '{:.0f}% - '.format(
                round(self.distribution[i][1] / self.shape[0], 2) * 100)
        return result[:-3]

    def __str__(self) -> str:
        return ("Name: {}\nShape: {}\nNumber of Clusters: {}\nDistribution: {}\nPossible pool_sizes: {}\n****************************\n").format(self.name, self.shape, len(self.distribution), self.distributionToString(), self.possiblePoolSizes())


def balanceInfo(Y_data) -> list:
    dataBalanceArr: list = []
    for y in Y_data:
        yType = y.__class__.__name__
        clasterNum = y if yType == 'str_' or yType == 'int_' or yType == 'float_' else int(y.item())
        for data in dataBalanceArr:
            if data[0] == clasterNum:
                data[1] += 1
                break
        else:
            dataBalanceArr.append([clasterNum, 1]) 
    return dataBalanceArr


ucr = UCR_UEA_datasets()


def load_ucr(dataset: str):
    x_val, y_val, x_train, y_train = ucr.load_dataset(dataset)
    X = x_train if x_val is None else np.concatenate((x_train, x_val))
    Y_data = y_train if y_val is None else np.concatenate((y_train, y_val))
    return X.shape, balanceInfo(Y_data)


def loadDatasets() -> int:
    datasetNumber: int = 1
    all_ucr_dataset_names: list[str] = ucr.list_datasets()
    totalCountOfDatasets: int = len(all_ucr_dataset_names)
    for datasetName in all_ucr_dataset_names:
        try:
            X_shape, distribution = load_ucr(datasetName)
        except:
            print("{}/{} failed".format(datasetNumber, totalCountOfDatasets))
            datasetNumber += 1
            continue
        DataSet(datasetName, X_shape, distribution).addToFinalList()
        print("{}/{} loaded".format(datasetNumber, totalCountOfDatasets))
        datasetNumber += 1
    return totalCountOfDatasets
