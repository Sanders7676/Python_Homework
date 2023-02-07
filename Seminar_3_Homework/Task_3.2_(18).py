# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.

# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9


available_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
given_number_X = int(input(f'Введите число X: '))

for el in available_list:
    if el == given_number_X:
        print(given_number_X)
        break
        

list_2 = []
q = 0
i = 0
for el in available_list:
    if el != given_number_X:
        if available_list[i] > given_number_X:
            q = available_list[i] - given_number_X
        else:
            q = given_number_X - available_list[i]
        
        list_2[i] = q
        i += 1

print(list_2)


