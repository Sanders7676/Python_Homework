# Задача 2.1[10]
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. 
# Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.

# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2


n_number_of_coins = int(input('Введите количество монет, лежащих на столе: '))

number_of_eagles = 0
number_of_tails = 0
current_coin = 1

for current_coin in range (1, n_number_of_coins + 1):
    side_of_coin = int(input(f'Введите положение монеты {current_coin}: 0 или 1: '))
    if side_of_coin == 1:
        number_of_eagles += 1
    else:
        number_of_tails += 1
    current_coin += 1

print(f'Количество монет с орлом - {number_of_eagles}')
print(f'Количество монет с решкой - {number_of_tails}')

if number_of_eagles <= number_of_tails:
    print(f'Количество монет, которые необходимо перевернуть - {number_of_eagles}')
else:
    print(f'Количество монет, которые необходимо перевернуть - {number_of_tails}')