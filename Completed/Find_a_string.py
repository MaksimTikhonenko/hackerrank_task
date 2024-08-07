# У цьому завданні користувач вводить рядок і підрядок. Ви маєте вивести кількість разів,
# коли підрядок зустрічається у заданому рядку. Перебір рядка відбуватиметься зліва направо, а не справа наліво.
# ПРИМІТКА: Літери в рядку чутливі до регістру.
# Формат вводу
# Перший рядок вводу містить оригінальний рядок. Наступний рядок містить підрядок.
# Обмеження
# 1 ≤ len(string) ≤ 200
# Кожен символ у рядку є ascii-символом.
# Формат виводу
# Виведіть ціле число, що вказує загальну кількість входжень підрядка в оригінальний рядок.
# Приклад вводу
# ABCDCDC
# CDC
# Приклад виводу
# 2
# Концепція
# Деякі приклади обробки рядків, такі як ці, можуть бути корисними.
# Є кілька нових концепцій:
# У Python довжина рядка знаходиться за допомогою функції len(s), де s - це рядок.
# Для перебору довжини рядка використовуйте цикл for:
# for i in range(0, len(s)):
# print(s[i])
# Функція range використовується для циклу по деякій довжині:
# range(0, 5)
# Тут цикл проходить від 0 до 4. 5 виключається.
#
#
def count_substring(string, sub_string):
    count = 0
    for el in range(len(string) - len(sub_string) + 1):
        if string[el:el + len(sub_string)] == sub_string:
            count += 1
    return count


c = "ABCDCDC"
v = "CDC"
print(count_substring(c, v))

# count = 0
# for el in range(len(c) - len(v) + 1):
#     if c[el:el + len(v)] == v:
#         count += 1
# print(count)
