
# Вам надано рядок, і ваше завдання - поміняти регістр.
# Іншими словами, перетворіть всі малі літери на великі, а великі - на малі.
# Наприклад:
# Www.HackerRank.com → wWW.hACKERrANK.cOM
# Pythonist 2 → pYTHONIST 2
# Опис функції:
# Завершіть функцію swap_case в редакторі нижче.
# swap_case має такі параметри:
#
# string s: рядок для модифікації
#
# Повертає:
#
# string: модифікований рядок
#
# Формат вводу:
# Один рядок, що містить рядок s.
# Обмеження:
# 0 < len(s) ≤ 1000
# Приклад вводу 0:
# HackerRank.com presents "Pythonist 2".
# Приклад виводу 0:
# hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(s):
    res = ""
    for el in s:
        if el.islower():
            res += el.upper()
        elif el.isupper():
            res += el.lower()
        else:
            res += el
    return res


a = input()
result = swap_case(a)
print(result)
