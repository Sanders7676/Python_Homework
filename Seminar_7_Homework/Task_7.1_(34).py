# 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами.

# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

# Примечание.

#     Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
#     Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.

# (*) Усложнение.

# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах. 
# Эта информация возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])


# Описание решения:

# 1) Задаем множество (set) гласных букв.
# 2) У нас есть строка ("..."), в строке есть пробелы, которые отделяют друг от друга "фразы"
# Строку нужно преобразовать в список так, чтобы фразы превратились в элементы списка.
# 3) Проходим по элементам списка и считаем сколько гласных букв в каждом элементе списка.
# Эти количества (по фразам) складываем в новый список. Т.е. элементы списка показывают количество гласных по фразам.
# 4) Этот новый список преобразуем в множество. 
# 5) Если в множестве 1 элемент значит количество гласных одинаковое. Выдаем True.
# Если больше 1, то количество гласных различается -> False

print()

def is_rithmic_chant(chant: str) -> None:    
    vowels = {'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'}
    phrases = list(chant.split())
    number_of_vowels_per_phrase = []
    
    for phrase in range(len(phrases)):
        num_of_vowels = 0
        for letter in phrases[phrase]:
            if letter in vowels:
                num_of_vowels += 1
        number_of_vowels_per_phrase.append(num_of_vowels)

    print(chant)
    # print(number_of_vowels_per_phrase)
    if len(set(number_of_vowels_per_phrase)) != 1: print(False)
    else: print(True)


is_rithmic_chant("пара-ра-рам рам-пам-папам па-ра-па-дам")
print()

is_rithmic_chant("пара-ра-рам рам-пум-пупам па-ре-по-дам")
print()

is_rithmic_chant("пара-ра-рам рам-пуум-пупам па-ре-по-дам")
print()

is_rithmic_chant("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па")
print()

is_rithmic_chant("Пам-парам-пурум Пум-пурум-карам")
print()