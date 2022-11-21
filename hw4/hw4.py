# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
# (Хеш то що з ліва записувати не потрібно)

# emails = []
#
# try:
#     with open('emails.txt', mode='r') as file:
#         for line in file:
#             if '@gmail.com' in line.split()[1]:
#                 emails.append(line.split()[1])
#
# except Exception as err:
#     print(err)
#
# try:
#     with open('gmails.txt', mode='w') as file:
#         for mail in emails:
#             file.writelines(f'{mail}\n')
#
# except Exception as err:
#     print(err)


# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

import json
import uuid


class Purchase:
    __book = []

    def __init__(self, name, price):
        self.__price = price
        self.__name = name
        self.__id = uuid.uuid4().int

    @classmethod
    def add_to_book(cls, self):
        cls.__book.append({'id': self.__id, 'name': self.__name, 'price': self.__price})
        try:
            with open('book.json', mode='w') as file:
                json.dump(cls.__book, file)
        except Exception as err:
            print(err)

    @classmethod
    def get_all(cls):
        for item in cls.__book:
            print(f'{item["name"]} - {item["price"]}')

    @classmethod
    def delete_by_id(cls, num):
        for i, v in enumerate(cls.__book):
            if v["id"] == num:
                cls.__book.pop(i)

        try:
            with open('book.json', mode='w') as file:
                json.dump(cls.__book, file)
        except Exception as err:
            print(err)

    @classmethod
    def find_max(cls):
        if len(cls.__book) != 0:
            max_price = max(cls.__book, key=lambda item: item['price'])
            print('*' * 20)
            print(f'{max_price["name"]} - {max_price["price"]}')
            print('*' * 20)

    @classmethod
    def find(cls, value):
        for item in cls.__book:
            for k, v in item.items():
                if k == 'price':
                    value = int(value)
                if v == value:
                    print('*' * 20)
                    print(f'{item["name"]} - {item["price"]}')
                    print('*' * 20)


# print('1. Add book\n'
#       '2. Get all books\n'
#       '3. Find a book with max price\n'
#       '4. Find a book by any value\n'
#       '5. Exit\n'
#       '********************************')
#
# while True:
#     x = input('Enter a number: ')
#
#     match x:
#         case '1':
#             n = input('Enter a name: ')
#             p = input('Enter a price: ')
#             Purchase.add_to_book(Purchase(n, int(p)))
#             print('*' * 20)
#             print(f'Added book: {n}')
#             print('*' * 20)
#         case '2':
#             Purchase.get_all()
#         case '3':
#             Purchase.find_max()
#         case '4':
#             key = input('Enter a value: ')
#             Purchase.find(key)
#         case '5':
#             print('Finish')
#             break
