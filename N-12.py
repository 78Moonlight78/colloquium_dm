# Задача N-12 "Остаток от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)"
# Выполнил Козориз К.И.
#
# Входные данные:
# Программа принимает на вход два массива целых чисел, представленных таким образом:
# Число n, обозначающее кол-во разрядов, и массив A[...] размера n, содержащий цифры в этих разрядах.
#
# Алгоритм:
# С помощью DIN_NN_N находим частное, проверяем не равно ли оно 0, если равно - значит наш массив меньше второго массива, поэтому он является остатком
# Если не равно 0 - с помощью SUB_NDN_N вычитаем из arr1 arr2
#
# Выходные данные:
# Программа возвращает массив целых чисел  - остаток от деления


def MOD_NN_N(n1, arr1, n2, arr2):
    b = arr1.copy()
    while n1 >= n2:
        arr1 = b.copy()
        a = DIV_NN_N(n1, arr1, n2, arr2)[1]
        arr1 = b

        if a[0] == 0:
            return arr1
        n1, b = SUB_NDN_N(n1, b, n2, arr2, 1)
        arr2.reverse()

    return arr1
    
    
    print(MOD_NN_N(4, [1, 8, 9, 0] , 2, [3, 1]))
    print(MOD_NN_N(4, [1, 0, 0, 0] , 2, [3, 3]))
