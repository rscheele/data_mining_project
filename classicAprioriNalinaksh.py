# Based on script by github user nalinaksh adaptation by Lisa Tostrams (august 2017)
# Written by Rodi Scheele (Januari 2018)
from __future__ import print_function

import itertools

def classic_apriori_nalinaksh(filename, support, confidence, maxr):
    # L1 = All frequent 1 itemsets > Support
    # D = All transactions
    L1, D, transactions = frequent_1_itemsets(filename, support)
    L = freq_itemsets(L1, support, D)
    return 0

def frequent_1_itemsets(filename, support):
    C1 = {} #item, it's transactions
    """total number of transactions contained in the file"""
    transactions = 0 #total number of transactions to calculate support
    D = [] # List of all transactions
    T = [] # list of transactions with item occurence
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

    L1=[] #C1 with low support items removed
    for key in C1.keys():
        if round(100.0 * len(C1[key]) / transactions, 2) >= support:
            sup = round(100.0 * len(C1[key]) / transactions, 2)
            transaction = (key, C1[key], sup)
            L1.append(transaction)

    L1.sort(key=lambda s:s[2],reverse=True)

    print("---------------TOP 10 FREQUENT 1-ITEMSET-------------------------")
    for i in range(0,10):
        print('Item ID=' + str(L1[i][0]) + ' Supp=' + str(L1[i][2]))
    print("-----------------------------------------------------------------")

    return (L1, D, transactions)

def freq_itemsets(L1, support, D):
    k = 2
    Lk_1 = []
    Lk = []
    L = []
    L.append(L1)
    count = 0
    transactions = 0
    support = 10
    for item in L1:
        Lk_1.append([item[0]])
    while Lk_1 != []:
        Ck = []
        Lk = []
        Ck = apriori_gen(Lk_1, k - 1)
        for c in Ck:
            count = 0
            transactions = 0
            s = set(c)
            for T in D:
                transactions += 1
                t = set(T)
                if s.issubset(t) == True:
                    count += 1
            if count >= support:
                c.sort()
                Lk.append((c, ('sup=', count, 2)))
        Lk_1 = []
        if (len(Lk) > 0):
            print("-------TOP 10 (or less) FREQUENT %d-ITEMSET------------------------" % k)
            print(*['set= {{ {} }},  {} {}'.format(', '.join(item[0]), item[1][0], item[1][1]) for item in
                    sorted(Lk, key=lambda item: item[1][1], reverse=True)][:10], sep='\n')
            print("------------------------------------------------------------------")
        for l in Lk:
            Lk_1.append(l[0])
        support = 10 * (k - 1)
        k += 1
        if Lk != []:
            L.append(Lk)

    return L

def apriori_gen(Lk_1, k):
    length = k
    Ck = []
    for list1 in Lk_1:
        for list2 in Lk_1:
            count = 0
            c = []
            if list1 != list2:
                while count < length-1:
                    if list1[count] != list2[count]:
                        break
                    else:
                        count += 1
                else:
                    if list1[length-1] < list2[length-1]:
                        for item in list1:
                            c.append(item)
                        c.append(list2[length-1])
                        if not has_infrequent_subset(c, Lk_1, k):
                            Ck.append(c)
                            c = []
    return Ck

def has_infrequent_subset(c, Lk_1, k):
    list = []
    list = set(itertools.combinations(c,k))
    for item in list:
        s = []
        for l in item:
            s.append(l)
        s.sort()
        if s not in Lk_1:
            return True
    return False


