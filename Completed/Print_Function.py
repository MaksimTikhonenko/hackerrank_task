
# "Включений кодовий фрагмент зчитає ціле число, , з STDIN.
#
# Не використовуючи жодних методів рядків, спробуйте вивести наступне:
#
# Зверніть увагу, що “” представляє послідовні значення між ними.
#
# Приклад
# n = 5
# Виведіть рядок 12345.
#
# Формат введення
# Перший рядок містить ціле число .
#
# Обмеження
#
# Формат виведення
#
# Виведіть список цілих чисел від до як рядок, без пробілів.
#
# Приклад вводу 3
#
# Приклад виведення 123


n = int(5)


def str_int(values):
    i = 1
    x = []
    while i < values + 1:
        x.append(str(i).replace('', ''))
        i = i + 1
    print(''.join(x))


str_int(n)
