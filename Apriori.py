# Apriori

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)


len(dataset)



    
transactions=[]

[transactions.append([str(dataset.values[i,j]) for j in range(20)]) for i in range(7501)]


# Training Apriori on our dataset

from apyori import apriori

rules = apriori(transactions, min_support= (0.003), min_confidence= 0.2 ,min_lift=3 , min_length = 2)

# Visualising the results
results = list(rules)

# Readable Results

results_list = []

for i in range(len(results)):

    results_list.append('RULE:\t' + str(results[i][0]) +

                        '\nSUPPORT:\t' + str(results[i][1]) +

                        '\nCONFIDENCE:\t' + str(results[i][2][0][2]) +

                        '\nLIFT:\t' + str(results[i][2][0][3]))
