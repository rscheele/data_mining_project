import itertools

list_of_transactions = 1
count = 0
item = 0
s = 0
support = 0
Lk = []

k = 1
T = list_of_transactions
for i in T:
    sup[i] = (count[i in T] / [count(T])
    if i > supoprt:
        Lk.append(i)
while True:
    k+=1
    Ck = list(itertools.combinations(Lk, k))
    for c in Ck:
        s = 0
        for t in T:
            if c.issubsetof(t) == True:
                s+=1
        if s > support:
            Lk.append(c)
    if Ck == []:
        break



k = 1
T = list_of_transactions
L1 = []
for i in T:
    sup[i] = (count[i in T] / [count(T])
    if i > supoprt:
        L1.append(i,[List_of_transactions_containing_i],support)
while True:
    k+=1
    L1 = []
    Ck = list(itertools.combinations(L1, k))
    for c in Ck:
        s = len(set(c.intersection(List_of_transactions_containing_i))
        if s > support:
            Lk.append(c)
            for i in c:
                if i not in L1:
                    L1.append(i)
    if L1 == []:
        break