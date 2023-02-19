# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии

# Программа принимает от пользователя три числа :

#     Первый элемент прогрессии, Разность (шаг) и Количество элементов

# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Напишите функцию

# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.

# Примеры/Тесты:

# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку, вам понадобится распаковка и Comprehension или map



print(' ')

print('Введите показатели арифметической прогрессии:')
first_element, progression_step, number_of_progression_elements = int(input(f'Первый элемент: ')), int(input(f'Шаг: ')), int(input(f'Количество элементов: '))

print(' ')

def forming_arithmetic_progression(first_element: int, progression_step: int, number_of_progression_elements: int) -> None:
  progression = []
  
  for index in range(number_of_progression_elements):
    current_element = first_element + progression_step * index
    progression.append(current_element)
  
  print(progression)

forming_arithmetic_progression(first_element, progression_step, number_of_progression_elements)

print(' ')


print('Введите через пробел показатели прогрессии: первый элемент, шаг и количество элементов:')
# Ввод показателей прогрессии в одну строку через Comprehension:
first_element, progression_step, number_of_progression_elements = [int(x) for x in input().split()]

# Ввод показателей прогрессии в одну строку через функцию map:
# first_element, progression_step, number_of_progression_elements = map(int, input().split())

print(' ')

# Формирование списка через Comprehension:
def forming_arithmetic_progression(first_element: int, progression_step: int, number_of_progression_elements: int) -> None:
  # progression = [first_element + progression_step * index for index in range(number_of_progression_elements)]
  # print(progression)
  print([first_element + progression_step * index for index in range(number_of_progression_elements)])  # Принт с Компрехеншеном внутри

forming_arithmetic_progression(first_element, progression_step, number_of_progression_elements)

print(' ')