
import operator
action = {
"+": operator.add,
"-": operator.sub,
"/": operator.truediv,
"*": operator.mul,
"**": pow
}
number1 = float(input("Введите первое число: "))

operat = input("Введите операцию:  ")

number2 = float(input("Введите второе число:  "))

result = action[operat](number1, number2)
print(result)




































