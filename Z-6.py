# Задача Z-6
# Выполнил Смирнов М.О.

# Входные данные:
# Программа принимает на вход два целых числа, массивы Z1[b, n; A[]] и Z1[b, n; A[]],
# где b - знак числа, n - номер старшей позиции в числе, A[] - массив цифр.

# Алгоритм:
# На входе программа проверяет, равны ли знаки у чисел, если да,
# то они складываются по алгоритму сложения натуральных чисел,
# если нет, то вычисляется, какое число больше:
# из большего числа вычитается меньшее по алгоритму вычитания натуральных чисел
# и подставлятся знак большего

# Выходные данные:
# Программа возвращает целочисленное значение суммы Z[b, n; A[]]

def ADD_ZZ_Z(b1, n1, A1, b2, n2, A2):
    # POZ_Z_D (Z-2) если оба числа однаковых знаков
    if POZ_Z_D(b1, n1, A1) == POZ_Z_D(b2, n2, A2):
        # то просто складываем как натуральные ADD_NN_N(Z1[1, 2], Z1[1, 2]) (N-4)
        N = ADD_NN_N(n1 , A1, n2, A2)
        Z = [b1, N[0], N[1]]
    else:
        # ABS_Z_N(Z-1) если числа равны по абсолютной величине, то возвращаем ноль
        if ABS_Z_N(b1, n1, A1) == ABS_Z_N(b2, n2, A2):
            Z = [0, 1, [0]]
        # если они разные, то вычисляем какое число больше
        elif COM_NN_D(n1, A1, n2, A2) == 2:
            # то вычитаем из большего меньшее по алгоритму SUB_NN_N(N-5)
            N = SUB_NN_N(n1, A1, n2, A2)
            Z = [b1, N[0], N[1]]
        else:
            N = SUB_NN_N(n2, A2, n1, A1)
            Z = [b2, N[0], N[1]]
    return Z

print(ADD_ZZ_Z(1, 4, [4,4,9,9], 1, 3, [3,9,9])) #[1, 4, [4, 8, 9, 8]]

print(ADD_ZZ_Z(0, 0, [0,0,0,0], 1,  3, [3,9,9])) #[1, 3, [3, 9, 9]]

print(ADD_ZZ_Z(1, 4, [4,4,9,9], 0, 3, [3,9,9])) #[1, 4, [4, 1, 0, 0]]

print(ADD_ZZ_Z(1, 8, [4,9,9,9,9,4,9,9], 0, 7, [3,9,9,9,9,9,9])) #[1, 8, [4, 5, 9, 9, 9, 5, 0, 0]]

print(ADD_ZZ_Z(1, 3, [4,9,9], 0, 3, [3,9,9])) #[1, 3, [1, 0, 0]]

print(ADD_ZZ_Z(1, 2, [9,7], 0, 3, [1,2,3])) #[0, 2, [2, 6]]

print(ADD_ZZ_Z(0, 2, [2,5], 1, 1, [9])) #[0, 2, [1, 6]]