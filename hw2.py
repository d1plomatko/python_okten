# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

# 2) протипізувати перше завдання

# =========================================================================================


from typing import Callable


def notebook() -> tuple[Callable[[str], list[str]], Callable[[], None]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> list[str]:
        todo_list.append(todo)
        return todo_list

    def get_all() -> None:
        print(todo_list)

    return add_todo, get_all


(add, get) = notebook()


#
# add('do hw')
# add('play games')
# get()
# add('watch movies')
# get()


# =========================================================================================

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# =========================================================================================

def expanded_form(num: int) -> None:
    print('+'.join(reversed([n + ('0' * i) for i, n in enumerate(str(num)[::-1]) if n != '0'])))


# expanded_form(12)
# # expanded_form(42)
# # expanded_form(70304)

# =========================================================================================

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій


def decor(func: Callable[[], Callable[[], None]]):
    count = 0

    def inner() -> None:
        nonlocal count
        print('*' * 20)
        func()
        count += 1
        print(f'Count: {count}')
        print('*' * 20)
        print()

    return inner


@decor
def greeting() -> None:
    print('hello world!')

# greeting()
# greeting()
# greeting()
