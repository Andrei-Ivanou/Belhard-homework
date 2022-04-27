"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(lst):
    for i in lst:
        if lst.count(i) > 1:
            return print("yes")
    return print("no")


print(yes_or_no([45,56,78,8,78,6,9,3,5,7,4]))