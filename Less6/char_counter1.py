"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'

def dickt(STR_VAL):
    k = {}
    for i in STR_VAL:
        if i in k:
            k[i] += 1
        else:
            k[i]=1
    return k

print(dickt(STR_VAL))

