# Ми бачили, що списки змінювані (їх можна змінювати), а кортежі незмінні (їх не можна змінювати).
# Давайте спробуємо зрозуміти це на прикладі.
# Вам дано незмінний рядок, і ви хочете внести в нього зміни.
# Приклад
#
# string = "abracadabra"
#
# Ви можете отримати доступ до індексу так:
#
# print string[5]
# a
#
# Що якщо ви хочете присвоїти значення?
#
# string[5] = 'k'
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
#
# Як би ви підійшли до цього?
#
# Одне рішення - конвертувати рядок у список, а потім змінити значення.
#
# Приклад
#
# string = "abracadabra"
# l = list(string)
# l[5] = 'k'
# string = ''.join(l)
# print string
# abrackdabra
#
#
# Інший підхід - розрізати рядок і з'єднати його назад.
#
# Приклад
#
# string = string[:5] + "k" + string[6:]
# print string
# abrackdabra

# Задача
# Прочитати заданий рядок, змінити символ за вказаним індексом, а потім вивести модифікований рядок.
# Опис функції
# Завершіть функцію mutate_string в редакторі нижче.
# mutate_string має такі параметри:
#
# string string: рядок для зміни
# int position: індекс для вставки символу
# string character: символ для вставки
#
# Повертає
#
# string: змінений рядок
#
# Формат вводу
# Перший рядок містить рядок string.
# Наступний рядок містить ціле число position, індекс розташування та рядок character, розділені пробілом.
# Приклад вводу
# STDIN       Функція
#
# abracadabra s = 'abracadabra'
# 5 k         position = 5, character = 'k'
# Приклад виводу
# abrackdabra


def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = ''.join(lst)
    return string


s = input("Enter string: ")
i, c = input("Enter position and character: ").split()
s_new = mutate_string(s, int(i), c)
print(s_new)
