# Задача P-12: " Производная многочлена"
# Здех К.В.
# Входные данные:
# Программа принимает на многочлен в виде массива:
# Алгоритм:
# циклом бежим по коэфицентам полинома
# умнажем их на степень слагаемого полинома
# умножение производится с с помощью функции  MUL_QQ_Q(умножение рац чисел)
# после чего возвращаем получившийся полином, у которго будет на 1 слагаемое меньше  
def DER_P_P(k,arr):
    for i in range(k,-1,-1):
        arr[k-i] = MUL_QQ_Q([i,1],arr[k-i])
    arr = arr[0:-1]
    return [k-1,arr]



