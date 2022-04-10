



def GCF_NN_N(n1, arr1, n2, arr2):
    while NZER_N_B(len(arr1), arr1) == True and NZER_N_B(len(arr2), arr2) == True:
        if COM_NN_D(len(arr1), arr1, len(arr2), arr2) == 2: #arr1 > arr2
            arr1 = MOD_NN_N(len(arr1), arr1, len(arr2), arr2)
        elif COM_NN_D(len(arr1), arr1, len(arr2), arr2) == 1: #arr1 < arr2
            arr2 = MOD_NN_N(len(arr2), arr2, len(arr1), arr1)
        else:
            return arr1
    else:
        if COM_NN_D(len(arr1), arr1, len(arr2), arr2) == 2: #arr1 > arr2
            return arr1
        else:
            return arr2
        return arr1, arr2

print(GCF_NN_N(4, [1, 0, 0, 0], 3, [5, 2, 5]))
