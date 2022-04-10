# Выполнил Серкин Д.А. 1310
# GCF_PP_P (P-11) НОД многочленов

# Входные данные (два многочлена)

# Алгоритм:
# Для реализации данной задачи будем использовать алгоритм Евклида

# Используемые модули: 
# DEG_P_N  Степень многочлена
# MOD_PP_P Остаток от деления многочлена на многочлен при делении с остатком

# Выходные данные (многочлен (m2, C2), представленный следующим образом):
# Многочлен с рациональными коэффициентами, m2 – степень многочлена и массив C2 коэффициентов



def GCF_PP_P(m1, C1, m2, C2):
    
    if m2 > m1:
        m1, m2 = m2, m1
        C1, C2 = C2, C1
    
    m3, C3 = MOD_PP_P(m1, C1, m2, C2)
    
    # Будем осуществлять деление до тех пор, пока остаток не равен нулю
    # 0 = 0, [0, 1, [0], 1, [1]]
    while m3 != 0 or C3 != [0, 1, [0], 1, [1]]:
        m1, C1 = m2, C2
        m2, C2 = m3, C3
        m3, C3 = MOD_PP_P(m1, C1, m2, C2)
        
    # Последний делитель(m2, C2) будет нашим НОД
    
    # Узнаем степень многочлена
    m2 = DEG_P_N(C2)
    if m2 == 0:
        C2[0] = 0
    return [m2, C2]
