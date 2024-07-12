#
# Вам дається рядок.
# Ваше завдання з’ясувати, чи містить рядок:
# буквено-цифрові символи, букви, цифри, малі та великі літери.

# 1/ string.isalnum()
# 2/ string.isalpha()
# 3/ string.isdigit()
# 4/ string.islower()
# 5/ string.isupper()


# У першому рядку надрукуйте True, якщо містить буквено-цифрові символи. В іншому випадку виведіть False.
# У другому рядку виведіть True, якщо є будь-які букви. В іншому випадку виведіть False.
# У третьому рядку виведіть True, якщо є якісь цифри. В іншому випадку виведіть False.
# У четвертому рядку надрукуйте True, якщо є якісь символи нижнього регістру. В іншому випадку виведіть False.
# У п’ятому рядку виведіть True, якщо є якісь символи верхнього регістру. В іншому випадку виведіть False.


# def string_validator_cb(input_str, test_cb):
#     # ch - character
#     for ch in input_str:
#         if test_cb(ch):
#             print(True)
#             return
#
#     print(False)
#
#
# inputs = input("Enter string: ")
#
#
# string_validator_cb(inputs, lambda x: x.isalnum())
# string_validator_cb(inputs, lambda x: x.isalpha())
# string_validator_cb(inputs, lambda x: x.isdigit())
# string_validator_cb(inputs, lambda x: x.islower())
# string_validator_cb(inputs, lambda x: x.isupper())

# TODO: Переписати код по прикладу!!!!


def str_validator_pro(input_str):
    tests = [lambda x: x.isalnum(),
             lambda x: x.isalpha(),
             lambda x: x.isdigit(),
             lambda x: x.islower(),
             lambda x: x.isupper()
             ]
    result = [False] * len(tests)

    for ch in input_str:
        for tests_inx in range(0, len(tests)):
            result[tests_inx] = result[tests_inx] or tests[tests_inx](ch)

    for r in result:
        print(r)
    print(f"{len(result)} results")


str_validator_pro('q2A87sdjlfnJFJKF^@#(')
