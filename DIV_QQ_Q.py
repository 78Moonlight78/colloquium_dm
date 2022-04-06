#Задача Q-8: Деление дробей (делитель отличен от нуля)
#Выполнил Чибисов А.А.

# Функция принимает на вход массив из 5 элементов: 
# Первый - знак
# Второй - кол-во цифр в числителе
# Третий - массив цифр числителя
# Четвёртый - кол-во цифр в знаменателе
# Пятый - массив цифр знаменателя

# Выходные данные:
# В результате программа возвращает массив из 5 элементов, описанных выше.

# Использованный модуль:
# MUL_ZZ_Z(умножение целых чисел)

def DIV_QQ_Q(A, B):
    # Если изначально две дроби имели разные знаки, то получившаяся дробь будет с минусом, иначе с плюсом.  
    if (A[0] == B[0]):
        sign = 0
    else:
        sign = 1
    # Делим дроби(числитель первой умножаенаем на знаменатель второй, знаменатель первой умножаем на числитель второй) используя функцию MUL_ZZ_Z.
    # Используем срез, чтобы присвоить переменной amount номер старшей позиции, а переменной number - массив цифр
    amount1, number1 = MUL_ZZ_Z(0, A[1], A[2], 0, B[3], B[4])[1:]
    amount2, number2 = MUL_ZZ_Z(0, B[1], B[2], 0, A[3], A[4])[1:]
    
    return [sign, amount1, number1, amount2, number2]


