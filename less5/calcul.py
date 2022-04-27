
import operator
action = {
"+": operator.add,
"-": operator.sub,
"/": operator.truediv,
"*": operator.mul,
"**": pow
}
print('Вас приветствует калькулятор')
a = input('Если не хотите использовать калькулятор наберите "стоп" ')
n = 0

while a != "stop" or a != "стоп":

    a = input('Если не хотите использовать калькулятор наберите "стоп": ')
    if a == "стоп" or a == "stop":
        print('всего вам хорошего')
        break
    else: print('lets go')
    n+=1
    print("Количество операций с калькулятором", n)
    try:
        num1 =int(input("Введите первое число : "))
        num2 = int(input("Введите второе число :  "))
        operat = input("Введите одну из операций +, *, -, / :  ")
    except ValueError:
        print("Неправильный ввод данных")
    if operat == "+":
        print(action[operat](num1, num2))
    elif operat == "-":
        print(action[operat](num1, num2))
    elif operat == "*":
        print(action[operat](num1, num2))
    elif operat == "/":
        if num2 != 0:
            print(action[operat](num1, num2))
        else:
             print("Деление с 0 невозможно")



