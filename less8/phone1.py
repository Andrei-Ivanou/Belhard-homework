"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

class Phone:

    def __init__(self, brand, model, issue_year, name):

        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.name = name

    def receive_call(self):
        print(f'Звонит - {self.name}')

    def get_info(self):
        return(self.brand, self.model, self.issue_year)

    def __str__(self):
        print(f"Информация:\nБрэнд - {self.brand}\n Модель -  {self.model}\n Год выпуска - {self.issue_year}")

iphone = Phone(" Яблоко", 10, 2018, "Andrei")

iphone.get_info()
iphone.__str__()
iphone.receive_call()