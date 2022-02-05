"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


def not_sort(obj):
    n = int(len(obj) / 2)
    max_number = 0
    for i in range(len(obj)):
        if obj[i] > max(obj):
            max_number = i
        if n + 1 >= len(obj):
            return obj[i]
    obj.pop(i)

def get_median(my_list, m):
    not_sort(my_list)
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
Время выполнения кода c m=10: 0.007683900000000004
Время выполнения кода c m=100: 0.33868489999999996
Время выполнения кода c m=1000: 30.1506401
"""
