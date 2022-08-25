#  UCR-DatasetAnalizer

I wrote this program to extract essential information about the datasets provided by "UCR_UEA_datasets."

Currently, this basic information contains:

1- Each dataset's name

2- Each dataset's shape

3- Number of clusters

4- Distribution of elements in each cluster

5- The list of possible pool_sizes for each dataset. 

(If we say in dataset X, each observation contains N time stamps, this list includes the divisors of N (except 1 and N itself). I needed this info in another project)


When the loading process is finished, the loaded datasets will be sorted based on the number of observations they contain.

The above information will be saved to a text file named "datasetInfo.txt"

I've added the results I got to this repository.

Please, note that in my case, 7 out of 115 datasets could not be loaded due to the "Permission Exception."


Arash Vashagh, Aug 2022
