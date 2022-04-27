
print('Вас приветствует калькулятор')
a = input('Если не хотите использовать калькулятор наберите "стоп" ')
n = 0
while a != "stop" or a != "стоп":

    a = input('Если не хотите использовать калькулятор наберите "стоп": ')
    if a == "стоп" or a == "stop":
        print('всего вам хорошего')
        break

    else: print('lets go')
    n += 1
    print("Количество операций с калькулятором", n)
    try:
        number = input("Введите данные в формате число действие число: ")
        print(eval(number))
    except (ValueError, NameError,SyntaxError):
        print("Неправильный ввод данных")







