# Задача N-13 "НОД натуральных чисел"
# Выполнил Козориз К.И.
#
# Входные данные:
# Программа принимает на вход два массива целых чисел, представленных таким образом:
# Число n, обозначающее кол-во разрядов, и массив A[...] размера n, содержащий цифры в этих разрядах.
#
# Алгоритм:
# Проверяем какое из двух чисел больше с помощтю функции COM_NN_D, идем в цикле while до того момента, пока arr1 и arr2 не равны нулю, при этом если arr1 > arr2 - записываем в arr1 остаток от деления arr1 на arr2, иначе наоборот, в конце выводим бОльшее из двух массивов
#
# Выходные данные:
# Программа возвращает массив целого числа - НОД arr1 и arr2



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
print(GCF_NN_N(3, [5, 2, 5], 4, [1, 0, 0, 0]))
