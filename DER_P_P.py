
def DER_P_P(k,arr):
    for i in range(k,-1,-1):
        arr[k-i] = MUL_QQ_Q([i,1],arr[k-i])


    arr = arr[0:-1]
    return [k-1,arr]

