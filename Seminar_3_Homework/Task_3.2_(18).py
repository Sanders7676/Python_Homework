# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.

# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9


available_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
given_number_X = int(input(f'Введите число X: '))

list_of_differences = []

for current_index in range(len(available_list)):
    if available_list[current_index] > given_number_X:
        difference = available_list[current_index] - given_number_X
    else:
        difference = given_number_X - available_list[current_index]
    list_of_differences.append(difference)

min_element_in_list_of_differences = list_of_differences[0]
desired_index_in_available_list= 0

for current_index in range(1, len(list_of_differences)):
    if list_of_differences[current_index] < min_element_in_list_of_differences:     
        min_element_in_list_of_differences = list_of_differences[current_index]
        desired_index_in_available_list = current_index

print(available_list[desired_index_in_available_list])