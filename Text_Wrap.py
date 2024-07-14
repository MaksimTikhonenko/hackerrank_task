# Перевірте вкладку "Посібник", щоб дізнатися, як розв'язати.

# Обтікання текстом
# Модуль textwrap надає дві зручні функції: wrap() і fill().
#
# textwrap.wrap()
# Функція wrap() обтікає один абзац у тексті (рядок) так, що кожен рядок має довжину не більше символів ширини.
# Він повертає список вихідних рядків.
#
# >>> import textwrap
# >>> string = "This is a very very very very very long string."
# >>> print textwrap.wrap(string,8)
# ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']
# textwrap.fill()
# Функція fill() обтікає один абзац у тексті та повертає один рядок, що містить перенесений абзац.
#
# >>> import textwrap
# >>> string = "This is a very very very very very long string."
# >>> print textwrap.fill(string,8)
# This is
# a very
# very
# very
# very
# very
# long
# string.

# Вам дано рядок S та ширину w.
# Ваше завдання - обгорнути рядок у параграф шириною w.
# Опис функції
# Завершіть функцію wrap в редакторі нижче.
# wrap має такі параметри:
#
# string string: довгий рядок
# int max_width: ширина, до якої треба обгорнути
#
# Повертає
#
# string: один рядок з символами нового рядка ('\n') там, де мають бути розриви
#
# Формат вводу
# Перший рядок містить рядок, string.
# Другий рядок містить ширину, max_width.
#
# Приклад вводу 0
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Приклад виводу 0
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap


def wrap(string, max_width):
    a = textwrap.fill(string, max_width)
    return a


stg, max__width = input(), int(input())
result = wrap(stg, max__width)
print(result)
