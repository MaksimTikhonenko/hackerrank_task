

# У Python рядок тексту можна вирівняти зліва, справа та по центру.
# .ljust(width)
# Цей метод повертає рядок, вирівняний по лівому краю, довжиною width.
# .center(width)
# Цей метод повертає рядок, вирівняний по центру, довжиною width.
# .rjust(width)
# Цей метод повертає рядок, вирівняний по правому краю, довжиною width.
# Завдання
# Вам дано частковий код, який використовується для генерації логотипу HackerRank змінної товщини.
# Ваше завдання - замінити пробіл (_____) на rjust, ljust або center.
# Формат вводу
# Один рядок, що містить значення товщини для логотипу.
# Обмеження
# Товщина повинна бути непарним числом.
# 0 < товщина < 50
# Формат виводу
# Вивести бажаний логотип.


# Replace all ______ with rjust, ljust or center.

thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
