"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""
def sum_number(num):
    sum = 0
    while num > 0:
        d = num % 10
        num = num // 10
        sum += d
    return print(sum)



print(sum_number(29))