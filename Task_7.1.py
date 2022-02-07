"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit

#Без доработки
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(100)]

print(f'Время выполнения кода без доработки: {timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000)} сек')
print(f'Исходный массив: {orig_list}')
bubble_sort(orig_list)
print(f'Новый массив: {orig_list}\n')

#С доработкой
def bubble_fixed(lst_obj):
    n = 1
    while n < len(lst_obj):
        count_sort = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                count_sort = False
        if count_sort == True:
            break
        n += 1
    return lst_obj

orig_list = [randint(-100, 100) for _ in range(100)]

print(f'Время выполнения кода c доработкой: {timeit("bubble_fixed(orig_list[:])", globals=globals(), number=1000)} сек')
print(f'Исходный массив: {orig_list}')
bubble_fixed(orig_list)
print(f'Новый массив: {orig_list}')

"""
Время выполнения скрипта с небольшим массивом с доработкой незначительно уменьшается (разница: без доработки 0.005 сек
и с доработкой 0.003 сек). На больших массивах замеры примерно одинаковы.
"""

