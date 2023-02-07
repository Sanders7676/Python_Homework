# 3.1[16]: Дан список целых чисел. Требуется вычислить, 
# сколько раз встречается некоторое число X в этом списке.

# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

# Примеры/Тесты:
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2

# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1

# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

# (*) Усложнение. При выводе результата на экран воспользуйтесь тернарным оператором.

given_number_X = int(input(f'Введите число X: '))
available_list = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]

repetitions_of_given_number = 0

for el in available_list:
    if el == given_number_X:
        repetitions_of_given_number += 1

if repetitions_of_given_number == 0:
    print(-1)
else:
    print(repetitions_of_given_number)

# Решение через тернарный оператор:

print('-1' if repetitions_of_given_number == 0 else repetitions_of_given_number)