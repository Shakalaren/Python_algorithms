"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""


from collections import deque
from timeit import timeit

my_list = [i for i in range(1000)]
deque_example = deque(my_list)


print('1) append, pop, extend')

def list_append():
    for i in range(1000):
        my_list.append(i)


def deque_append():
    for i in range(1000):
        deque_example.append(i)

print(f'Длительность выполнения метода append в list: {timeit("list_append()", globals=globals(), number=1000)}')
print(f'Длительность выполнения метода append в deque: {timeit("deque_append()", globals=globals(), number=1000)}\n')


def list_pop():
    for i in range(1000):
        my_list.pop()


def deque_pop():
    for i in range(1000):
        deque_example.pop()


print(f'Длительность выполнения метода pop в list: {timeit("list_pop()", globals=globals(), number=1000)}')
print(f'Длительность выполнения метода pop в deque: {timeit("deque_pop()", globals=globals(), number=1000)}\n')

def list_extend():
    for i in range(1000):
        my_list.extend([i for i in range(10)])


def deque_extend():
    for i in range(1000):
        deque_example.extend([i for i in range(10)])


print(f'Длительность выполнения метода extend в list: {timeit("list_extend()", globals=globals(), number=1000)}')
print(f'Длительность выполнения метода extend в deque: {timeit("deque_extend()", globals=globals(), number=1000)}\n')


# Данные операции и у списка и у дека выполняются примерно одинаково по времени


print('2) appendleft, popleft, extendleft')

def list_appendleft():
    for i in range(100):
        my_list.insert(0, i)


def deque_appendleft():
    for i in range(100):
        deque_example.appendleft(i)


print(f'Длительность выполнения метода insert в list: {timeit("list_appendleft()", globals=globals(), number=10)}')
print(f'Длительность выполнения метода appendleft в deque: {timeit("deque_appendleft()", globals=globals(), number=10)}\n')

def list_popleft():
    for i in range(100):
        my_list.pop(0)


def deque_popleft():
    for i in range(100):
        deque_example.popleft()

print(f'Длительность выполнения метода pop в list: {timeit("list_popleft()", globals=globals(), number=10)}')
print(f'Длительность выполнения метода popleft в deque: {timeit("deque_popleft()", globals=globals(), number=10)}\n')


def list_extendleft():
    for i in range(100):
        for i in range(10):
            my_list.insert(0, i)


def deque_extendleft():
    for i in range(100):
        deque_example.extendleft([i for i in range(10)])


print(f'Длительность выполнения метода insert в list: {timeit("list_extendleft()", globals=globals(), number=10)}')
print(f'Длительность выполнения метода extendleft в deque: {timeit("deque_extendleft()", globals=globals(), number=10)}\n')


# Данные операции у дека выполняются гораздо быстрее


print('3) операции получения элемента')


def list_set():
    for i in range(1000):
        my_list[i] = 0


def deque_set():
    for i in range(1000):
        deque_example[i] = 0


print(f'Длительность получения элемента в list: {timeit("list_set()", globals=globals(), number=1000)}')
print(f'Длительность получения элемента в deque: {timeit("deque_set()", globals=globals(), number=1000)}\n')


# Операции получения элементы быстрее выполняются у списка