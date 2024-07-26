#
# Враховуючи таблицю результатів учасників для вашого Університетського дня спорту,
# ви повинні знайти результат, який посідає друге місце. Вам дають n балів.
# Збережіть їх у списку та знайдіть оцінку гравця, який посів друге місце.
#
# Формат введення
#
# Перший рядок містить n.
# Другий рядок містить масив A[ ] із n цілих чисел, кожне з яких розділено пробілом.

# Формат виводу
# Роздрукуйте рахунок, який посів друге місце.

# sample input
# 5
# 2 3 6 6 5

# sample output
# 5

# Даний список [2, 3, 6, 6, 5]. Максимальний бал – 6,
# другий максимум – 5. Тому ми друкуємо 5 як другий бал.


n = int(5)  # Це кількість балів (елементів) у списку
arr = [2, 3, 6, 6, 5]


def sort_sports_day(x):
    set_list = set(x)
    norm_list = list(set_list)
    sort_list = sorted(norm_list, reverse=True)
    second_max_val = sort_list[1]
    print(second_max_val)


sort_sports_day(arr)


def sort_s_day(input_list):
    dict_list = dict.fromkeys(input_list)
    norm_list = list(dict_list)
    sort_list = sorted(norm_list)
    second_max_val = sort_list[-2]
    print(second_max_val)


sort_s_day(arr)


def new_sort_s_day(input_list):
    lst = []
    for el in input_list:
        if el not in lst:
            lst.append(el)
    sort_list = sorted(lst)

    second_max_val = sort_list[-2]
    print(second_max_val)


new_sort_s_day(arr)
