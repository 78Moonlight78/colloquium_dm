def FAC_P_Q(C):
    A = [0]     # НОК и НОД не могут быть отрицательными
    numers = []     # числители
    denoms = []     # знаменатели
    for i in range(1, C[0] + 2):
        numers.append(C[i][1:1 + 2])
        denoms.append(C[i][3:3 + 2])
    a = GCF_NN_N(numers[0][0], numers[0][1], numers[1][0], numers[1][1])    # пара в числителе и зн-ле точно будет
    b = LCM_NN_N(denoms[0][0], denoms[0][1], denoms[1][0], denoms[1][1])
    if len(numers) > 2:
        for i in range(2, len(numers)):
            a = GCF_NN_N(a[0], a[1], numers[i][0], numers[i][1])
    if len(denoms) > 2:
        for i in range(2, len(denoms)):
            b = LCM_NN_N(b[0], b[1], denoms[i][0], denoms[i][1])
    for i in range(2):   # наверное можно проще
        A.append(a[i])
    for i in range(2):
        A.append(b[i])
    return A