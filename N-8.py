# N-8 "Умножение натуральных чисел"
# автор: Пелагейко Анастасия, 1310

# функция получает на вход номер старшей позиции в натуральном числе (кол-во цифр в числе) 'n'
# и два массива (списка) цифр в натуральном числе ('А' и 'B')

def MUL_NN_N(n1, A, n2, B):
    # пустой список, в котором будет храниться результат умножения
    mul0 = []
    # сдвиг разряда (0 - единицы, 1 - десятки и т.д.)
    k = 0

    # если одно из чисел равно нулю
    if A == [0] or B == [0]:
        # c2 - количество цифр в произведении A * B
        c2 = 1
        # массив чисел с результатом умножения теперь хранит только 0
        mul0.insert(0, 0)
    else:
        # удобнее умножать большое число на цифры маленького, так как потребуется меньше итераций в цикле
        # и потебуется складывать меньшее количество слагаемых

        # если первое число меньше второго - меняем их местами
        if COM_NN_D(n1, A, n2, B) == 1:
            A, B = B, A
            #temp - буферная переменная для переприсваивания
            temp = n1
            n1 = n2
            n2 = temp

        for i in range(len(B)-1, -1, -1):
            # перемножаем первое введённое натуральное число поочерёдно с каждой цифрой из второго числа
            # начиная с конца второго числа

            # используется функция умножения натурального числа на цифру 'MUL_ND_N'
            # c - количество цифр в произведении после умножения натурального числа на цифру
            c, L = MUL_ND_N(len(A), A, B[i])
            A.reverse()  # не относится к основному алгоритму

            # сдвигаем разряд произведения, умножив полученное слагаемое на 10^k

            # используется функция умножения натурального числа на 10^k 'MUL_Nk_N'
            # с1 - количество цифр в произведении после умножения натурального числа на 10^k
            c1, L = MUL_Nk_N(c, L, k)

            # складываем полученные результаты произведений (сумма накапливается в массиве mul0)

            # используется функция сложения натуральных чисел 'ADD_NN_N'
            c2, mul0 = ADD_NN_N(len(mul0), mul0, c1, L)

            # увеличиваем сдвиг на 1
            k = k + 1
    return [c2, mul0]
