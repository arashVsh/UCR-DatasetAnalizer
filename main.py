import numpy as np
from Dataset import *


def printResult(totalCountOfDatasets: int):
    print("\nAll Datasets: ", totalCountOfDatasets)
    acceptedDatasetsCnt = len(ACCEPTED_DATASETS)
    print("Loaded Datasets: ", acceptedDatasetsCnt)
    print("Failed Datasets: ", totalCountOfDatasets - acceptedDatasetsCnt)


def writeToFile():
    fileName: str = "datasetInfo.txt"
    with open(fileName, "w") as file_object:
        for i in range(len(ACCEPTED_DATASETS)):
            file_object.write(str(i + 1) + '\n' +
                              ACCEPTED_DATASETS[i].__str__())
    print("Saved to {}".format(fileName))


if __name__ == "__main__":
    totalCountOfDatasets = loadDatasets()
    printResult(totalCountOfDatasets)
    writeToFile()
