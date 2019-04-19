# Written by Rodi Scheele (Januari 2018)
from __future__ import print_function

import itertools

def improved_apriori_adaptation(filename, support, confidence, maxr):
    # L1 = All frequent 1 itemsets > Support
    # D = All transactions
    L1, D, transactions = frequent_1_itemsets(filename, support)
    L = freq_itemsets(L1, support)
    return 0

def frequent_1_itemsets(filename, support):
    C1 = {} #item, it's transactions
    """total number of transactions contained in the file"""
    transactions = 0 #total number of transactions to calculate support
    D = [] # List of all transactions
    T = [] # list of transactions with item occurence
    # Add all the transactions to a big list with the item as ID and a list of transactions it occurs in
    with open(filename, "r") as f:
        for line in f:
            T = []
            for word in line.split(','):
                word = word.rstrip()
                T.append(word)
                if word not in C1.keys():
                    C1[word] = [transactions]
                else:
                    C1[word].append(transactions)

            transactions += 1
            D.append(T)

    L1=[] # Contains item ID, transactions and support where items with < support are pruned
    for key in C1.keys():
        if round(100.0 * len(C1[key]) / transactions, 2) >= support:
            sup = round(100.0 * len(C1[key]) / transactions, 2)
            transaction = (key, C1[key], sup)
            L1.append(transaction)

    L1.sort(key=lambda s:s[2],reverse=True)
    # printing things
    print("---------------TOP 10 FREQUENT 1-ITEMSET-------------------------")
    for i in range(0,10):
        print('Item ID=' + str(L1[i][0]) + ' Supp=' + str(L1[i][2]))
    print("-----------------------------------------------------------------")

    return (L1, D, transactions)

def freq_itemsets(L1, support):
    k = 2
    support = 10 # hardcoded for this dataset
    Lk = []
    L = [] # contain a set for each k-size itemset, each set for the k contains all k-size itemsets

    while True:
        # Create all possible itemsets with L1
        Ckc = list(itertools.combinations(L1, k))
        # Prune itemsets in Ck that were not in Lk-1 if Lk > 1, otherwise don't prune
        Ck = []
        if k > 2:
            for c in Ckc: # For each item in our candidate itemset
                ids = []
                b = False
                for i in c: # Create a list of item ids from the candidate
                    ids.append(i[0])
                z = set(ids)
                for l in Lk: # For each itemset from our previous k-1 itemset check if the candidate has it as subset
                    x = set(l[0])
                    if x.issubset(z): # Check if the k candidate itemset has a subset somewhere in k-1 itemsets
                        b = True
                        break # No need to scan any further if a subset was found, save some processing power
                if b:
                    Ck.append(c) # If a subset was found in the k candidate itemset it is added to our new candidate set
        else: # Don't want pruning for C2 so Ck = Ckc for C2
            Ck = Ckc

        L1 = [] # L1 and Lk need to be emptied for (possible) next cycle
        Lk = []

        for i in range(0, len(Ck)): # For each itemset in candidate itemset
            transactionlist = []
            idList = []
            s = 0
            for j in range(0, len(Ck[i])): # Create seperate list with id's and transactions
                idList.append(Ck[i][j][0])
                transactionlist.append(Ck[i][j][1])
            s = len(set(transactionlist[0]).intersection(*transactionlist[1:])) # Check for intersection between all transactions for each candidate itemset
            if (s >= support): # If number of intersections > support it is added to frequent k-size itemset
                Lk.append((idList,s))
                for m in range(0, len(Ck[i])):
                    if Ck[i][m] not in L1:
                        L1.append(Ck[i][m]) # create a new L1 for only items in k-size itemsets
        L.append(Lk) # add all k-size itemsets to a set that contains a set for each k
        support = 10 * (k - 1)
        k += 1
        if L1 == []: # if none k-size itemsets were found break out of the loop
            Lk = []
            break

    p = 2 #printing things
    for i in range(0,len(L)-1):
        L[i].sort(key=lambda s:s[1],reverse=True)
        if len(L[i]) > 10:
            k = 10
        else:
            k = len(L[i])
        print("---------------TOP 10 FREQUENT %d-ITEMSET-------------------------" % p)
        for j in range(0,k):
            print('Item ID=' + str(L[i][j][0]) + ' Supp=' + str(L[i][j][1]))
        print("-----------------------------------------------------------------")
        p+=1
    return L
