"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from timeit import timeit
from random import randint

def gnome(obj):
    i, size = 1, len(obj)
    while i < size:
        if obj[i - 1] <= obj[i]:
            i += 1
        else:
            obj[i - 1], obj[i] = obj[i], obj[i - 1]
            if i > 1:
                i -= 1
    return obj


def get_median(my_list, m):
    gnome(my_list)
    return my_list[m]

m=10
my_list_10 = [randint(0, 100) for x in range(2*m+1)]
print(f'Время выполнения кода c m=10: {timeit("get_median(my_list_10[:], m)", globals=globals(), number=1000)}')

m = 100
my_list_100 = [randint(0, 100) for x in range(2*m+1)]
print(f'Время выполнения кода c m=100: {timeit("get_median(my_list_100[:], m)", globals=globals(), number=1000)}')

m = 1000
my_list_1000 = [randint(0, 100) for x in range(2*m+1)]
print(f'Время выполнения кода c m=1000: {timeit("get_median(my_list_1000[:], m)", globals=globals(), number=1000)}')

"""
Результаты:
Время выполнения кода c m=10: 0.0167544
Время выполнения кода c m=100: 1.8779884
Время выполнения кода c m=1000: 225.6090716
"""
