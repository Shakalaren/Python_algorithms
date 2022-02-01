"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import Timer

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


t1 = Timer(stmt='func_1', setup="from __main__ import func_1")
print("func_1", t1.timeit(number=10000000), "seconds")


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


t2 = Timer(stmt='func_2', setup="from __main__ import func_2")
print("func_2", t2.timeit(number=10000000), "seconds")


def func_3():
    return f'Чаще всего появляется число {max(array, key=array.count)}'


t3 = Timer(stmt='func_3', setup="from __main__ import func_3")
print("func_3", t1.timeit(number=10000000), "seconds")

print(func_1())
print(func_2())
print(func_3())

"""
func_1 0.0925199 seconds
func_2 0.0903792 seconds
func_3 0.08939360000000002 seconds

По времени func_3 выполняется немного быстрее, чем остальные функции. Сложность также наименьшая среди всех функций у 
func_3 - O(n).
"""