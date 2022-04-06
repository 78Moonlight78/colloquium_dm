# Задача P-5: Старший коэффициент многочлена
# Выполнил Егоров И.М

# Входные данные:
# Программа принимает на вход C - массив коэффициентов многочлена.
# То есть массив коэффициентов начинается с наибольшей степени многочлена

# Алгоритм:
# Получаем на вход массив коэффициентов. Возвращаем нулевой элемент трехмерного массива. (Старший коэффициент многочлена)

# Выходные данные:
# Возвращаем старший кооэффициент многочлена (нулевой элемент массива)

m = 4
C = [[0,2,[4,5],1,[2]],[0,2,[4,3],1,[1]],[0,1, [2],1,[1]],[0,1, [0],1,[1]],[0,1, [1],1,[1]]]
def LED_P_Q(C):    
    return C[0]

print(LED_P_Q(C))
