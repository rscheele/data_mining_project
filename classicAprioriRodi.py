# Based on script by github user nalinaksh
from __future__ import print_function

import itertools

def classic_apriori_rodi(filename, support, confidence, maxr):
    # L1 = All frequent 1 itemsets > Support
    # D = All transactions
    L1, D, transactions = frequent_1_itemsets(filename, support)
    L = freq_itemsets(L1, support, D)
    return 0

def frequent_1_itemsets(filename, support):
    C1 = {} #item, it's transactions
    transactions = 0 # total amount of transactions
    D = [] # List of all transactions
    T = [] # list of transactions with item occurence
    with open(filename, "r") as f:
        for line in f:
            T = []
            transactions += 1
            for word in line.split(','):
                word = word.rstrip()
                T.append(word)
                if word not in C1.keys():
                    C1[word] = 1
                else:
                    count = C1[word]
                    C1[word] = count + 1
            D.append(T)

    L1=[] #C1 with low support items removed
    for key in C1:
        C1sup = round(100.0 * C1[key] / transactions, 2)
        if C1sup >= support:
            item = (key, C1sup)
            L1.append(item)

    L1.sort(key=lambda s:s[1],reverse=True)

    print("---------------TOP 10 FREQUENT 1-ITEMSET-------------------------")
    for i in range(0,10):
        print('Item ID=' + str(L1[i][0]) + ' Supp=' + str(L1[i][1]))
    print("-----------------------------------------------------------------")

    L1_nosupp = [] # remove support values from L1, just keep ID's
    for i in L1:
        L1_nosupp.append(i[0])

    return (L1_nosupp, D, transactions)

def freq_itemsets(L1, support, D):
    k = 2
    support = 10 # hardcoded for this dataset
    Lk = []
    L = [] # contain a set for each k-size itemset, each set for the k contains all k-size itemsets

    while True:
        # Create all possible itemsets with L1 or Lk-1
        Ckc = list(itertools.combinations(L1, k))

        # Prune itemsets in Ck that were not in Lk-1 if Lk > 1, otherwise don't prune
        Ck = []
        if k > 2:
            for c in Ckc: # For each item in our candidate itemset
                b = False
                z = set(c)
                for l in Lk: # For each itemset from our previous k-1 itemset check if the candidate has it as subset
                    x = set(l)
                    if x.issubset(z): # Check if the k candidate itemset has a subset somewhere in k-1 itemsets
                        b = True
                        break # No need to scan any further if a subset was found, save some processing power
                if b:
                    Ck.append(c) # If a subset was found in the k candidate itemset it is added to our new candidate set
        else: # Don't want pruning for C2 so Ck = Ckc for C2
            Ck = Ckc

        L1 = [] # L1 and Lk need to be emptied for (possible) next cycle
        Lk = []
        Lk_supp = []

        for i in Ck: # For each itemset in candidate itemset
            s = 0
            c = set(i) #candidate
            for T in D:
                t = set(T)
                if c.issubset(t):
                    s+=1
            if (s >= support): # If number of intersections > support it is added to frequent k-size itemset
                Lk_supp.append((i,s))
                Lk.append(i)
                for m in i:
                    if m not in L1:
                        L1.append(m) # create a new L1 for only items in k-size itemsets

        if Lk == []: # if none k-size itemsets were found break out of the loop
            break
        else:
            support = 10 * (k-1)
            k += 1
            L.append(Lk_supp)  # add all k-size itemsets to a set that contains a set for each k

    p = 2 #printing things
    for i in range(0,len(L)):
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



