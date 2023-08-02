#  UCR-DatasetAnalizer

I developed this program to extract vital information about the datasets provided by "UCR_UEA_datasets."

The extracted information includes the following for each dataset:

1. Name of the dataset
2. Shape of the dataset
3. Number of clusters
4. Distribution of elements in each cluster
5. List of possible pool_sizes for each dataset (excluding 1 and the dataset's total number of time stamps, N)

This information was required for another project, where the pool_sizes' divisors were relevant.

Upon completion of the loading process, the loaded datasets will be sorted based on the number of observations they contain.

The results obtained have been added to this repository.

Please note that, in my case, 7 out of 115 datasets could not be loaded due to a "Permission Exception."

Arash Vashagh, Aug 2022
