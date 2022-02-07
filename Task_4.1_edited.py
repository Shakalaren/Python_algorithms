"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import Timer, timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# t1 = Timer(stmt="func_1", setup="from __main__ import func_1")
# print("func_1 ", t1.timeit(number=10000000), "seconds")

print(timeit("func_1", globals=globals(), number=1000))


def func_2(nums):
    my_arr = [i for i in nums if nums[i] % 2 == 0]
    return my_arr


# t2 = Timer(stmt='func_2', setup="from __main__ import func_2")
# print("func_2", t2.timeit(number=10000000), "seconds")

print(timeit("func_2", globals=globals(), number=1000))

"""
Учитывая, что и func_1 и func_2 являются встроенными функциями, оптимизированными по времени, быстрее будет выполняться 
func_2, так как это list comprehension, а он выполняется быстрее, чем итератор с функцией append (func_1).
"""
