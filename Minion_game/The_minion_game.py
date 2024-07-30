
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


def count_words(input_word):
    len_input = len(input_word)
    stuart_score = 0
    kevin_score = 0
    for idx in range(len_input):
        current_letter = input_word[idx]
        words_count = len_input - idx
        if current_letter[0] in {'A', 'E', 'I', 'O', 'U'}:
            kevin_score += words_count
        else:
            stuart_score += words_count

    return stuart_score, kevin_score


def minion_game(st):
    res_stuart, res_kevin = count_words(st)

    if res_kevin > res_stuart:
        result = 'Kevin ' + str(res_kevin)
    elif res_kevin == res_stuart:
        result = 'Draw'
    else:
        result = 'Stuart ' + str(res_stuart)
    print(result)
    return result


s = 'BANANA'
minion_game(s)
