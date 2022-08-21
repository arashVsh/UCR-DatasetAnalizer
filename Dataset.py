ACCEPTED_DATASETS: list = []

class DataSet:
    def __init__(self, name: str, shape) -> None:
        self.name = name
        self.shape = shape

    def possiblePoolSizes(self) -> list[int]:
        allDivisors: list[int] = []
        numberOfTimeSteps = self.shape[1]
        for i in range(2, numberOfTimeSteps // 2 + 1):
            if numberOfTimeSteps % i == 0:
                allDivisors.append(i)
        return allDivisors

    def addToFinalList(self): # Sorts the list based on the number of observations
        for i in range(len(ACCEPTED_DATASETS)):
            if self.shape[0] > ACCEPTED_DATASETS[i].shape[0]:
                ACCEPTED_DATASETS.insert(i, self)
                return
        ACCEPTED_DATASETS.append(self)

    def __str__(self) -> str:
        return ("Name: {}\nShape: {}\nPossible pool_sizes: {}\n****************************\n").format(self.name, self.shape, self.possiblePoolSizes())
