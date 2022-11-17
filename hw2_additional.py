# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
#


def fibonacci(num: int) -> None:
    num1, num2 = 0, 1

    if num == 0:
        print(0)
    else:
        for i in range(num):
            print(num1)
            nth = num1 + num2
            num1 = num2
            num2 = nth


# fibonacci(12)


# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3

def even_odd_counter(num: int) -> None:
    even = 0
    odd = 0

    for item in list(str(num)):
        if int(item) % 2 == 0:
            even += 1
        else:
            odd += 1

    print(even, odd)

    # even_odd_counter(225688)
    # even_odd_counter(33294)

    # найти со списка только уникальные числа
    #
    # пример [1,2,3,4,2,5,1] => [ 3, 4, 5 ]


ls1 = [1, 2, 3, 4, 2, 5, 1]


def unique_nums(ls: list[int]) -> None:
    print(list(set(ls)))

# unique_nums([1, 2, 3, 4, 2, 5, 1])


def printer_error(s):
    count = 0
    txt = list(set(s))
    for letter in txt:
        if letter >= 'a' and letter <= 'm':
            count += 1
    print(f'{(len(s)- count)}/{len(s)}')


printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
