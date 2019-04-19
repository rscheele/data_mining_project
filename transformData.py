import numpy as np
import pandas as pd

'''DateTime, CustomerID, Product Subclass, ProductID'''
D01 = pd.DataFrame(pd.read_csv('Data/D01.txt', sep=';', header=0, names=['DateTime','CustomerID','ProductSubclass', 'ProductID'], usecols=(0,1,4,5)))
D02 = pd.DataFrame(pd.read_csv('Data/D02.txt', sep=';', header=0, names=['DateTime','CustomerID','ProductSubclass', 'ProductID'], usecols=(0,1,4,5)))
D11 = pd.DataFrame(pd.read_csv('Data/D11.txt', sep=';', header=0, names=['DateTime','CustomerID','ProductSubclass', 'ProductID'], usecols=(0,1,4,5)))
D12 = pd.DataFrame(pd.read_csv('Data/D12.txt', sep=';', header=0, names=['DateTime','CustomerID','ProductSubclass', 'ProductID'], usecols=(0,1,4,5)))

groupedData = np.asmatrix(D01.groupby(['DateTime','CustomerID']))

# 5.000 transactions
transactionData = []
for i in range(0,10000):
    transaction = np.asmatrix(groupedData.item(i))
    if transaction.shape[1] == 4:
        list = []
        for j in range(0,transaction[:,3].size):
            list.append(transaction[j,3])
        transactionData.append(list)
df = pd.DataFrame(transactionData)
np.savetxt('Data/transactions_D01_5000.txt', transactionData, fmt='%s')

# 15.000 transactions
transactionData = []
for i in range(0,30000):
    transaction = np.asmatrix(groupedData.item(i))
    if transaction.shape[1] == 4:
        list = []
        for j in range(0,transaction[:,3].size):
            list.append(transaction[j,3])
        transactionData.append(list)
df = pd.DataFrame(transactionData)
np.savetxt('Data/transactions_D01_15000.txt', transactionData, fmt='%s')

# 29.901 transactions
transactionData = []
for i in range(0,groupedData.size):
    transaction = np.asmatrix(groupedData.item(i))
    if transaction.shape[1] == 4:
        list = []
        for j in range(0,transaction[:,3].size):
            list.append(transaction[j,3])
        transactionData.append(list)
df = pd.DataFrame(transactionData)
np.savetxt('Data/transactions_D01_29901.txt', transactionData, fmt='%s')

# D01 and D02 merged - 60.952 transactions
mergedData = pd.concat([D01,D02])
groupedData = np.asmatrix(mergedData.groupby(['DateTime','CustomerID']))

transactionData = []
for i in range(0,groupedData.size):
    transaction = np.asmatrix(groupedData.item(i))
    if transaction.shape[1] == 4:
        list = []
        for j in range(0,transaction[:,3].size):
            list.append(transaction[j,3])
        transactionData.append(list)
df = pd.DataFrame(transactionData)
np.savetxt('Data/transactions_D01D02_60952.txt', transactionData, fmt='%s')

# D01, D02, D11, D12 merged - 119.578 transactions
mergedData = pd.concat([D01,D02,D11,D12])
groupedData = np.asmatrix(mergedData.groupby(['DateTime','CustomerID']))

transactionData = []
for i in range(0,groupedData.size):
    transaction = np.asmatrix(groupedData.item(i))
    if transaction.shape[1] == 4:
        list = []
        for j in range(0,transaction[:,3].size):
            list.append(transaction[j,3])
        transactionData.append(list)
df = pd.DataFrame(transactionData)
np.savetxt('Data/transactions_D01D02D11D12_119578.txt', transactionData, fmt='%s')