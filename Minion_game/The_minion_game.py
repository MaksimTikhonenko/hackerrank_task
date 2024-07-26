#
# Кевін та Стюарт хочуть зіграти в "Гру Міньйонів".
# Правила гри:
#
# Обом гравцям дається однаковий рядок, S.
# Обидва гравці повинні створювати підрядки, використовуючи літери рядка S.
# Стюарт має створювати слова, що починаються з приголосних.
# Кевін має створювати слова, що починаються з голосних.
# Гра закінчується, коли обидва гравці створили всі можливі підрядки.
#
# Підрахунок балів:
# Гравець отримує +1 бал за кожне входження підрядка в рядок S.
# Наприклад:
# Рядок S = BANANA
# Слово Кевіна, що починається з голосної = ANA
# Тут ANA зустрічається двічі в BANANA. Отже, Кевін отримає 2 бали.
# Ваше завдання - визначити переможця гри та його рахунок.
# Опис функції:
# Заповніть функцію minion_game в редакторі нижче.
# minion_game має наступні параметри:
#
# рядок string: рядок для аналізу
#
# Виводить:
#
# рядок: ім'я переможця та рахунок, розділені пробілом в одному рядку, або
# "Draw" (Нічия), якщо немає переможця
#
# Формат вводу:
# Один рядок вводу, що містить рядок S.
# Примітка: Рядок S буде містити лише великі літери: [A - Z].
# Обмеження:
# 0 < len(S) ≤ 10^6
# Приклад вводу:
# BANANA
# Приклад виводу:
# Stuart 12


def minion_game(st):
    # sub = build_substring(st)

    name = 'Stuart', 'Kevin'

    a = 0
    b = 0
    result = [a, b, 'Draw']

    stuart = []  # Витягти
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                  'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    for el in st:
        if el is consonants:
            a = a + 1

    # Порівняти Stuart\Kevin

    kevin = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    for el in st:
        if el is vowels:
            b = b + 1

# todo-----------------------
    # Вивести і'мя переможця
    # if res_kevin > res_stuart:
    #     print('Kevin' res_kevin)
    #     if res_kevin == res_stuart
    #          print('Draw')
    # else:
    #     print('Stuart' res_stuart)


# sub_kevin = build_substring(s)
# sub_stuart = build_substring(s)
#
# res_kevin = calculate_score(sub_kevin, filter_kevin)
# res_stuart = calculate_score(sub_stuart, filter_kevin)
# todo-------------------------------

s = 'BANANA'
minion_game(s)

# -------------------------------

filter_stuart = lambda x: x[0] not in 'AEIOUaeiou'
filter_kevin = lambda x: x[0] in 'AEIOUaeiou'


def calculate_score(input_str, substrings, condition):
    result = 0
    input_str = list(filter(condition, substrings))
    for _ in input_str:
        result = result + 1
    return result


# -------------------------------


def build_substring(input_word):
    result = []
    l_n = len(input_word)

    for el in range(l_n):
        for ele in range(el, l_n):
            result.append(input_word[el:ele + 1])

    return result


# print(build_substring('BAN'))
# print(calculate_score('BAN', ['B', 'BA', 'BAN', 'A', 'AN', 'N'], filter_stuart))


# sub_kevin = build_substring(s)
# sub_stuart = build_substring(s)
#
# res_kevin = calculate_score(sub_kevin, filter_kevin)
# res_stuart = calculate_score(sub_stuart, filter_kevin)
