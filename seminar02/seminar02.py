"""
CP1404 Seminar 2
Low High Random warmup program
"""


# # import random
# from random import randint
# 
# low_number = int(input("Enter a low number: "))
# high_number = int(input("Enter a high number: "))
# while low_number >= high_number:
#     print("Error. The higher number is less than or equal to the higher number.")
#     high_number = int(input("Enter a high number: "))
# random_number = randint(low_number, high_number)

# print(":)" * random_number)
# # for i in range(random_number):
# #     print(":)", end="")
# print()


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_even(number):
    """Determine if number is even."""
    if number % 2 == 0:
        return True
    return False


def is_even(number):
    return number % 2 == 0
