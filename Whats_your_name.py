
# Вам дано ім'я та прізвище особи у двох різних рядках. Ваше завдання - прочитати їх та вивести наступне:
# Hello firstname lastname! You just delved into python.
# Опис функції
# Завершіть функцію print_full_name в редакторі нижче.
# print_full_name має наступні параметри:
#
# string first: ім'я
# string last: прізвище
#
# Виводить
#
# string: 'Hello firstname lastname! You just delved into python',
# де firstname та lastname замінюються на first та last.
#
# Формат вводу
# Перший рядок містить ім'я, а другий рядок містить прізвище.
# Обмеження
# Довжина імені та прізвища кожного ≤ 10.
# Приклад вводу 0
# Ross
# Taylor
# Приклад виводу 0
# Hello Ross Taylor! You just delved into python.
# Пояснення 0
# Вхідні дані, прочитані програмою, зберігаються як тип даних string. Рядок - це набір символів.


def print_full_name(first, last):
    result = "Hello " + str(first) + " " + str(last) + "!" + " " + "You just delved into python."
    string = str(result)
    return string


first_name = input("Введіть ім'я: ")
last_name = input("Введіть прізвище: ")


print(print_full_name(first_name, last_name))
