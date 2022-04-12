# Q-1 "Сокращение дроби"
# автор: Пелагейко Анастасия, 1310

# функция получает на вход массив из 5 элементов:
# 1: 0, если числитель дроби положителен, 1 - если отрицателен (Q[0])
# 2: количество цифр в числителе (Q[1])
# 3: массив цифр числителя (Q[2])
# 4: количество цифр в знаменателе (Q[3])
# 5: массив цифр знаменателя (Q[4])

def RED_Q_Q(Q):
    # получаем абсолютное число числителя (получаем натуральное число),
    # используя функцию, возвращающую абсолютную величину числа, 'ABS_Z_N' (результат - натуральное)
    Q[1], Q[2] = ABS_Z_N(Q[0], Q[1], Q[2])

    # получаем НОД числителя и знаменателя,
    # используя функцию, возварщающую НОД натуральных чисел, 'GCF_NN_N'
    # cA - количество цифр в НОД числителя и знаменателя, nodA - массив чисел НОД-а,
    cA, nodA = GCF_NN_N(Q[1], Q[2], Q[3], Q[4])

    # делим абстолютное значение чилителя и знаменатель на НОД числителя и знаменателя,
    # используя функцию, возвращающую частное от деления целого на целое, 'DIV_ZZ_Z'
    # т.к. знаменатель - натуральное, а в ф-ии 'DIV_ZZ_Z' - целое, то в качестве знака знаменателя передаём 0
    Q[1], Q[2] = DIV_NN_N(Q[1], Q[2], cA, nodA)
    Q[3], Q[4] = DIV_NN_N(Q[3], Q[4], cA, nodA)

    # возвращаем сокращённую дробь
    return Q

