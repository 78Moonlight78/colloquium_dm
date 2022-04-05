# Задача Z-3: "Умножение целого на (-1)"
# Выполнил Серкин Д.А.

# Входные данные:
# Программа принимает на вход целое число представленное следующим образом:
# Целое число (b, n; A[..]) - знак числа (1 — минус, 0 — плюс), номер старшей позиции и массив цифр

# Алгоритм:
# Исходя из условия программа меняет значение переменной b на "противоположное" (1 на 0, 0 на 1)

# Выходные данные:
# В результате программа возвращает целое число представленное следующим образом:
# Целое число (b, n; A[..]) - знак числа (1 — минус, 0 — плюс), номер старшей позиции и массив цифр


def MUL_ZM_Z(b, n, A):
    return [1, n, A] if b == 0 else [0, n, A]

