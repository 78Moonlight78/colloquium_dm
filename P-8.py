# P-8 / MUL_PP_P
# Использованные модули: MUL_QQ_Q, ADD_PP_P
# Выполнил: Волосевич А.Н. (1310)


def MUL_PP_P(m1: int, C1: list, m2: int, C2: list) -> tuple:

    # Определене степени итогового многочлена
    res_m = m1 + m2

    # Определение итогового многочлена (пока состоящего из нулей)
    res_C = [[0, 1, [0], 1, [1]]] * (res_m + 1)



    # Перемножение элементов исходных массивов с помощью 2х циклов for:

    for ind_1 in range(m1+1): # Цикл по первому исходному массиву

        # Определене степени промежуточного многочлена
        mid_m = ind_1 + m2

        # Определение промежуточного многочлена
        mid_C = [[]] * (mid_m + 1)

        for ind_2 in range(m2+1): # Цикл по второму исходному массиву

            # Сохранение промежуточного результа
            mid_C[ind_1+ind_2] =  MUL_QQ_Q(C1[ind_1], C2[ind_2]) # Перемножение коэффициентов

        # Сумма каждого промежуточного результата с текущим многочленом:
        res_C = ADD_PP_P(res_m, res_C, mid_m, mid_C)

    return res_m, res_C




