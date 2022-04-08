# Задача N-10: "Вычисление первой цифры деления большего натурального на меньшее,
# домноженное на 10^k,где k - номер позиции этой цифры (номер считается с нуля)"
# Выполнил Поллуксов А.В.

# Входные данные:
# Программа принимает на вход 2 натуральных числа, представленных следующим образом:
# Целое число (n; arr[..]) - номер старшей позиции и массив цифр

# Алгоритм:
# 1)Возьмём у максимального числа нужное количество цифр для деления на меньшее (фактически, это деление "в столбик")
# 2)Найдём k: вычтем из количества цифр в максимальном числе количество цифр для деления на меньшее
# 3)Найдём первую цифру деления

# Выходные данные:
# Первая цифра деления и k

def DIV_NN_Dk(n1, arr1, n2, arr2):
    num = 0
    num_list = []
    temp = []
    chk = COM_NN_D(n1, arr1, n2, arr2)
    if chk == 2:
        min_num = arr2
        n2 = len(min_num)
        max_num = arr1
    elif chk == 1:
        min_num = arr1
        n2 = len(min_num)
        max_num = arr2
    else:
        return [1, [0]]      # Если число делится само на себя, k = 0

    # Минимальное не должно быть равно 0
    if not sum(min_num):
        raise ZeroDivisionError

    # Если нужно найти первую цифру деления на 1
    if sum(min_num) == 1:
        num_list.append(max_num[0])
        return MUL_Nk_N(1, num_list, len(max_num) - 1)

    # Берём у большего числа цифры для деления на меньшее
    for i in range(len(min_num)):
        temp.append(max_num[i])

    n_temp = len(temp)

    # Если цифр для деления на меньшее не хватило, возьмём ещё одну
    if COM_NN_D(n_temp, temp, n2,  min_num) == 1:
        temp.append(max_num[n_temp])
        n_temp += 1

    k = len(max_num) - n_temp

    # Деление в столбик
    while COM_NN_D(n_temp, temp, n2,  min_num) != 1:
        n_temp, temp = SUB_NN_N(n_temp, temp, n2, min_num)
        num += 1

    return [num, k]
