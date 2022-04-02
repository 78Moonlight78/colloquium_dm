Сложение натуральных чисел(N-4)
Выполнил: Ескин Кирилл
# С помощью функции map преобразовываем всё в строку, после чего с помощью join соединяем строку и преобразовываем в тип int, затем складываем.

def ADD_NN_N(arr1,arr2):
  result = int(''.join(map(str, arr1)))+int(''.join(map(str, arr2)))
  print(result)
  return result
ADD_NN_N([1,2,3],[4,5,6])
