"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, author: str, title: str, year: int):
        self.author = author
        self.title = title
        self.year = year

    def __str__(self):
         return f"{self.__author} {self.__title} {self.__year}"

    def __repr__(self):
         return f"{self.__author} {self.__title} {self.__year}" + "\n"

    def __eq__(self, other):
        return self.__year == other.__year

    def __gt__(self, other):
         return self.__year > other.__year

    def __lt__(self, other):
         return self.__year < other.__year

    def get_info(self):
        print(f"Aвтор - {self.__author}\n Hазвание книги - {self.__title}\n год издания - {self.__year}")


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val):
        if type(val) is str:
            self.__author = val
        else:
            raise TypeError('Неверный тип')

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val):
        if type(val) is str:
            self.__title = val
        else:
            raise ValueError("Неверный ввод")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        if type(val) is int:
            if CURRENT_YEAR >= val > 0:
                self.__year = val
            else:
                raise ValueError("Неверное значение даты")
        else:
            raise TypeError("Неверный тип")



b1 = BookCard("Vasili", "Don", 1945)
b2 = BookCard("Petr", "Donat", 2003)
b3 = BookCard("Igor", "Front", 1996)
b4 = BookCard("Pavel", "Fronter", 2014)
b5 = BookCard("Illy", "Prom", 2001)
b6 = BookCard("rtort", "Doni", 1989)

bl = [b1, b2, b3, b4, b5, b6]
#bl.sort()
bl.sort(key= lambda x: x.year)
print(b2 < b4)
print(bl)

