
# Задача P-12: " Производная многочлена"
# Здех К.В.
# Входные данные:
# Программа принимает на многочлен в виде массива:
# Алгоритм:
# Циклом бежим по элементам масива начиная с последнего
# Обнуляем счетчик
# Циклом бежим по элементам масива отвечающего за значения числителя коэфицента и складывая элементы получаем сам числитель
# Умнажаем числитель на степень слагаемого которому он пренадлежит
# Создаем массив  из элементов нового числителя
# меняем новый числитель на старый
# меняем первый элемент массива отвечающий за наибольшую степень на 1
# изменям сам массив удаляя последний элемент, так как он обнулился
def DER_P_P(arr):
    k = 1
    for i in range(arr[0],-1,-1):
        sum = 0
        for j in range(0,arr[k][1]):
            sum += arr[k][2][j]*(10**(arr[k][1]-j-1))
        sum *= i
        sum = str(sum)
        arr[k][1] = len(sum)
        z = []
        for j in range(0, len(sum)):
            z.append(int(sum[j]))
        arr[k][2] = z
        k += 1
    arr[0] -= 1
    arr = arr[0:-1]
    print(arr)
    return arr





