# У Python рядок можна розділити за роздільником.
# Приклад:
#
#
# a = "this is a string"
# a = a.split(" ") # a перетворюється на список рядків.
# print a
# ['this', 'is', 'a', 'string']
#
#
# З'єднання рядка просте:
#
#
# a = "-".join(a)
# print a
# this-is-a-string
#
#
#
# Завдання
# Вам дано рядок. Розділіть рядок за роздільником " " (пробіл) та з'єднайте, використовуючи дефіс.
# Опис функції
# Завершіть функцію split_and_join у редакторі нижче.
# split_and_join має наступні параметри:
#
# string line: рядок слів, розділених пробілами
#
# Повертає
#
# string: результуючий рядок
#
# Формат вводу
# Один рядок містить рядок, що складається зі слів, розділених пробілами.
# Приклад вводу
# this is a string
# Приклад виводу
# this-is-a-string


def split_and_join(line):
    string_line = line.split(" ")
    string = "-".join(string_line)
    return string


s_r = input("Введіть рядок: ")
result = split_and_join(s_r)
print(result)