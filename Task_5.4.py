"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {i: i for i in range(1000)}
my_ordict = OrderedDict(my_dict)

def dict_get():
    for i in range(1000):
        my_dict.get(i)


def ordict_get():
    for i in range(1000):
        my_ordict.get(i)


print(f'Длительность выполнения get в dict: {timeit("dict_get()", globals=globals(), number=1000)}')
print(f'Длительность выполнения get в OrderedDict: {timeit("ordict_get()", globals=globals(), number=1000)}\n')


def dict_change():
    for i in range(1000):
        my_dict[i] = 0


def ordict_change():
    for i in range(1000):
        my_ordict[i] = 0


print(f'Длительность выполнения изменения в dict: {timeit("dict_change()", globals=globals(), number=1000)}')
print(f'Длительность выполнения изменения в OrderedDict: {timeit("ordict_change()", globals=globals(), number=1000)}\n')


def dict_delete():
    my_dict_copy = my_dict.copy()
    for i in range(1000):
        my_dict_copy.pop(i)


def ordict_delete():
    my_ordict_copy = my_ordict.copy()
    for i in range(1000):
        my_ordict_copy.pop(i)


print(f'Длительность выполнения метода pop в dict: {timeit("dict_delete()", globals=globals(), number=1000)}')
print(f'Длительность выполнения метода pop в OrderedDict: {timeit("ordict_delete()", globals=globals(), number=1000)}\n')

# По времени выполнения dict явно показывает лучшие результаты. OrderedDict можно использовать, если важно указать на 
# упорядоченность, а также иметь возможность контроллировать порядок с помощью особых методов OrderedDict. В остальных
# случаях, стаднартный dict наиболее оптимальное решение.