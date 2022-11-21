# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'

# numbers = []
# for num in st:
#     if num.isdigit():
#         numbers.append(num)
# print(','.join(numbers))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st2 = 'as 23 fdfdg544 34'

numbers = []

for word in st2.split():
    num = ''
    for item in word:
        if item.isdigit():
            num = num + item
    numbers.append(num)
print(','.join(numbers).lstrip(','))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'

# l1 = [letter.upper() for letter in greeting]
# print(l1)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#

l2 = [i ** 2 for i in range(50) if i % 2 != 0]

# print(l2)

# function
#
# - створити функцію яка виводить ліст

numbers = [1, 2, 3, 4, 5]


def func(nums):
    print(nums)


# func(numbers)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.


def func2(a, b, c):
    print(max(a, b, c))
    return max(a, b, c)


# func2(1, 2, 3)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше


def func3(*args):
    print(max(args))
    return min(args)


# func3(1, 2, 3)


# - створити функцію яка повертає найбільше число з ліста


def max_num(nums):
    return max(nums)


# max_num(numbers)


# - створити функцію яка повертає найменьше число з ліста


def min_num(nums):
    return min(nums)


# min_num(numbers)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


def sum_num(nums):
    return sum(nums)


# sum_num(numbers)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.


def average(nums):
    return sum(nums) // len(nums)


# average(numbers)

#
#
#
#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число

list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# print(min(list))

#   - видалити усі дублікати

# print(set(list))

#   - замінити кожне 4-те значення на 'X'

# count = 3

# while count < len(list):
#     list[count] = 'x'
#     count += 4

# print(list)


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції


def square(num):
    print('*' * num)
    i = 0
    while i < (num - 2):
        print('*', ' ' * (num - 4), '*')
        i += 1
    print('*' * num)


# square(10)

# 3) вывести табличку множення за допомогою цикла while

i = 1
while i < 10:
    print(' '.join([f'{(i * num): 3}' for num in range(1, 10)]))
    i += 1

# 4) переробити це завдання під меню
#

# while True:
#     print('1. Знайти мінімільне число')
#     print('2. Видалити усі дублікати')
#     print('3. Замінити кожне 4 значення на х')
#     print('4. Вивести квадрат')
#     print('5. Вивести таблицю')
#     print('6. Вихід')
#
#     num = input('Вкажіть число: ')
#     if num == '1':
#         print(min(list))
#     elif num == '2':
#         print(set(list))
#     elif num == '3':
#         count = 3
#
#         while count < len(list):
#             list[count] = 'x'
#             count += 4
#
#         print(list)
#     elif num == '4':
#         square(10)
#     elif num == '5':
#         i = 1
#         while i < 10:
#             print([i * num for num in range(1, 10)])
#             i += 1
#     else:
#         break
