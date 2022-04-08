# Задача N-9: "Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом"
# Выполнил Кашуба Д.А.

# Входные данные:
# Программа принимает на вход два натуральных числа, представленных следующим образом и число D, на которое умножается:
# Целое число (n1; arr1[..]) - длина числа и массив цифр
# Целое число (n2; arr2[..]) - длина числа и массив цифр
# D - число, на котрое необхожимо умножить

# Алгоритм:
# Умножаем на число, с помощью функции MUL_ND_N, вычитаем, с помощью функции SUB_NN_N, в которой уже есть проверка на то, равны ли числа
# Выходные данные:
#  n_res - длина числа
#  A_res - результат вычитания


def SUB_NDN_N(n1, A1, n2, A2, D):
    A_res = []
    n2, A2 = MUL_ND_N(n2, A2, D)
    n_res, A_res = SUB_NN_N(n1, A1, n2, A2)
    return n_res, A_res

print(SUB_NDN_N(4, [1, 0, 0, 0], 3, [2,5,0], 3))  # проверка 1000 - 3 * 250 = 250
