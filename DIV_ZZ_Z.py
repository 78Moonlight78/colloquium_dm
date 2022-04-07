# Задача Z-9: "Частное от деления целого на целое"
# Выполнил Шлом И. М.

# Входные данные:
# Программа принимает на вход два целых число, представленных следующим образом:
# Целое число (b; n; A[..]) - знак перед числом (1 - минус, 0 - плюс), номер старшей позиции и массив цифр

# Алгоритм:
# 1. Создаются натуральные версии обоих полученных чисел
# 2. Проверяется знак у чисел, полученных на вход
# 2. Если знаки совпали, выполняется алгоритм деления натурального числа на натуральное с последующим превращением
# результата в целое число
# 3. Если знаки не совпали, выполняется алгоритм деления натуральных чисел, после которого к результату прибавляется 1,
# далее результат переводится в целое число и у него заменяется знак
# 4. Возвращается полученное частное

# Выходные данные:
# Целое число (b; n; A[..]) - знак, номер старшей позиции и массив цифр - результат целочисленного деления.


def DIV_ZZ_Z(b_1, n_1, A_1, b_2, n_2, A_2):
    res = 0
    nat_1 = ABS_Z_N(b_1, n_1, A_1)
    nat_2 = ABS_Z_N(b_2, n_2, A_2)
    if POZ_Z_D(b_1, n_1, A_1) == POZ_Z_D(b_2, n_2, A_2) == 2 or POZ_Z_D(b_1, n_1, A_1) == POZ_Z_D(b_2, n_2, A_2) == 1:
        res = DIV_NN_N(nat_1[0], nat_1[1], nat_2[0], nat_2[1])
        res = TRANS_N_Z(res[0], res[1])
    elif (POZ_Z_D(b_1, n_1, A_1) == 1 and POZ_Z_D(b_2, n_2, A_2) == 2) or (POZ_Z_D(b_1, n_1, A_1) == 2 and POZ_Z_D(b_2, n_2, A_2) == 1):
        res = DIV_NN_N(nat_1[0], nat_1[1], nat_2[0], nat_2[1])
        res = ADD_1N_N(res[0], res[1])
        res = TRANS_N_Z(res[0], res[1])
        res[0] = 1
    return res

