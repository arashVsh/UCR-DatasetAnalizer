import numpy as np
from Dataset import *
from tslearn.datasets import UCR_UEA_datasets

ucr = UCR_UEA_datasets()

def load_ucr(dataset: str):
    try:
        X_test, _, X_train, _ = ucr.load_dataset(dataset)
        X = np.concatenate((X_train, X_test))
    except:
        raise Exception("Access Denied!")
    return X.shape


def loadDatasets():
    datasetNumber: int = 1
    all_ucr_dataset_names: list[str] = ucr.list_datasets()
    totalCountOfDatasets: int = len(all_ucr_dataset_names)
    for datasetName in all_ucr_dataset_names:
        try:
            X_shape = load_ucr(datasetName)
        except:
            print("Progress: {}/{} failed".format(datasetNumber, totalCountOfDatasets))
            datasetNumber += 1
            continue
        DataSet(datasetName, X_shape).addToFinalList()
        print("Progress: {}/{} loaded".format(datasetNumber, totalCountOfDatasets))
        datasetNumber += 1
    return totalCountOfDatasets, len(ACCEPTED_DATASETS),


def printResult(allDatasetsCnt: int, acceptedDatasetsCnt: int):
    print("Total Number of Datasets: ", allDatasetsCnt)
    print("Number of Loaded Datasets: ", acceptedDatasetsCnt)
    print("Number of Failed Datasets: ", allDatasetsCnt - acceptedDatasetsCnt)


if __name__ == "__main__":
    allDatasetsCnt, acceptedDatasetsCnt = loadDatasets()
    printResult(allDatasetsCnt, acceptedDatasetsCnt)
    with open("datasetInfo.txt", "w") as file_object:
        for i in range(acceptedDatasetsCnt):
            file_object.write(str(i + 1) + '\n' +
                              ACCEPTED_DATASETS[i].__str__())
    print("Finished Writing To File")

