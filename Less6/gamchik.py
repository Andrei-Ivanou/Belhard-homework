
def bread(func):              # функция декоратор хлеб
    def wrapper():
        print("</------------\\>")
        func()
        print("<\\____________/>")
    return wrapper()

def tom(func):                 # функция декоратор томаты
    def wrapper():
        print("*** помидоры ****")
        func()
    return wrapper


def sal(func):                # функция декоратор салат
    def wrapper():
        print("~~~~ салат ~~~~~")
        func()
    return wrapper


def chess(func):               # функция декоратор сыр
    def wrapper():
        print("^^^^^ сыр ^^^^^^")
        func()
    return wrapper


def oni(func):               # функция декоратор лук
    def wrapper():
        print("----- лук ------")
        func()
    return wrapper


#def func():                           #функция beef
   # return print("### говядина ###")

def func():                          # функция chiken
    return print("|||| курица ||||")


#@bread
#@oni
#@tom
#def func():
    #print("### говядина ###")

@bread
@chess
@sal
def func():
    print("|||| курица ||||")

