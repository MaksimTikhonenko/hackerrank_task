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


def build_substring(input_word):
    result = []
    l_n = len(input_word)

    for el in range(l_n):
        for ele in range(el, l_n):
            result.append(input_word[el:ele + 1])

    return result


def calculate_score(substrings, condition):
    result = 0
    # if substrings != str():
    #     print("substrings no good")
    i = list(filter(condition, substrings))
    for _ in i:
        result = result + 1
    return result


def minion_game(st):
    sub = build_substring(st)

    filter_stuart = lambda x: x[0] not in 'AEIOUaeiou'
    filter_kevin = lambda x: x[0] in 'AEIOUaeiou'

    res_kevin = calculate_score(sub, filter_kevin)
    res_stuart = calculate_score(sub, filter_stuart)

    # Порівняти Stuart\Kevin Вивести і'мя переможця

    if res_kevin > res_stuart:
        result = ('Kevin', res_kevin)
    elif res_kevin == res_stuart:
        result = 'Draw'
    else:
        result = ('Stuart', res_stuart)
    return print(result)


s = 'BANANA'
minion_game(s)


# -------------------------------
#
# filter_stuart = lambda x: x[0] not in 'AEIOUaeiou'
# filter_kevin = lambda x: x[0] in 'AEIOUaeiou'
#
#
# def calculate_score(substrings, condition):
#     result = 0
#     # if substrings != str():
#     #     print("substrings no good")
#     i = list(filter(condition, substrings))
#     for _ in i:
#         result = result + 1
#     return result
#
#
# # -------------------------------
#
#
# def build_substring(input_word):
#     result = []
#     l_n = len(input_word)
#
#     for el in range(l_n):
#         for ele in range(el, l_n):
#             result.append(input_word[el:ele + 1])
#
#     return result
#

# print(build_substring('BAN'))
# print(calculate_score(['B', 12, 'BA', 'BAN', 'A', 'AN', -4, 'N'], filter_stuart))
