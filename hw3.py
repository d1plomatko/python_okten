from abc import ABC, abstractmethod


# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#  при виклику метода len() підраховувати сумму сторін

class Rectangle:

    def __init__(self, _x: int, _y: int):
        self._y = _y
        self._x = _x

    def area(self) -> int:
        return self._x * self._y

    def __add__(self, other) -> int:
        return self.area() + other.area()

    def __sub__(self, other) -> int:
        return self.area() - other.area()

    def __eq__(self, other) -> bool:
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        return self.area() != other.area()

    def __gt__(self, other) -> bool:
        return self.area() > other.area()

    def __lt__(self, other) -> bool:
        return self.area() < other.area()

    def __len__(self) -> int:
        return self._x * 2 + self._y * 2


rectangle1: Rectangle = Rectangle(10, 2)
rectangle2: Rectangle = Rectangle(5, 3)


# print(rectangle1.area())
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 > rectangle2)
# print(rectangle1 < rectangle2)
# print(len(rectangle1))

# ===========================================================================

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення


class Human:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name


class Prince(Human):
    def __init__(self, name: str, age: int, find_size: int):
        super().__init__(name, age)
        self.find_size = find_size

    def find_cinderella(self, c_list: list) -> str:
        for c in c_list:
            if c.foot_size == self.find_size:
                return c.name


class Cinderella(Human):
    _count: int = 0

    def __init__(self, name: str, age: int, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella._count += 1

    @classmethod
    def get_count(cls):
        return cls._count


cinderellas: list[Cinderella] = [Cinderella('Vika', 16, 36), Cinderella('Kira', 20, 37)]
prince1: Prince = Prince('Vasya', 22, 36)


# print(prince1.find_cinderella(cinderellas))
# print(Cinderella.get_count())


# =========================================================================================

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
# класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def print(self):
        print(self.name)

    def __init__(self, name: str):
        self.name = name


class Magazine(Printable):
    def print(self):
        print(self.name)

    def __init__(self, name: str):
        self.name = name


class Main:
    _printable_list: list[Magazine | Book] = []

    @classmethod
    def add(cls, element: Magazine | Book):
        if isinstance(element, (Book, Magazine)):
            cls._printable_list.append(element)

    @classmethod
    def show_all_magazines(cls):
        for item in cls._printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls._printable_list:
            if isinstance(item, Book):
                item.print()

# Main.add(Magazine('Magazine1'))
# Main.add(Magazine('Magazine2'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine4'))
# Main.add(Magazine('Magazine5'))
# Main.add(Magazine('Magazine6'))
# Main.add(Book('Book1'))
# Main.add(Book('Book2'))
# Main.add(Book('Book3'))
# Main.add(Book('Book4'))
# Main.add(Book('Book5'))
# Main.add(Book('Book6'))
# Main.show_all_magazines()
# print('*' * 20)
# Main.show_all_books()
