# 5.2[28]: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Циклы использовать нельзя

# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3


# Принцип решения задачи: 
# За одно действие второе число уменьшается на 1, а первое увеличивается на 1. 
# Когда второе число уменьшится до 0, первое число будет представлять собой сумму двух первоначальных чисел.
# Т.е. имеем два контейнера: из второго перекладываем предметы в первый.
# Когда второй контейнер опустеет в первом будут все предметы из обоих контейнеров.

def sum(a: int, b: int) -> int:
    if b == 0:                      # В опустело => всё в А
        return a
    else:
        return sum(a + 1, b - 1)    # Перекладываем из B в A 
        
print(sum(3, 0))