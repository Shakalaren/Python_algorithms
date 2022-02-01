
"""
из Task_1.2
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

from pympler import asizeof

#Было:

#Первый алгоритм O(n^2):
my_list = [10, 20, 300, -1, -5, 1]
print(f'Память обычного списка равна: {asizeof.asizeof(my_list)}')
mins = my_list[0]
for i in my_list:
    if i < mins:
        mins = i

print(mins)

#Второй алгоритм O(n):
my_list = [10, 20, 300, -1, -5, 1]
mins = my_list[0]
for i in my_list:
    if i < -1:
        print(i)

#Стало:
#Первый алгоритм:
def create_list(numbers):
    my_list = [num for num in range(numbers)]
    print(f'Память после ленивого вычисления равна: {asizeof.asizeof(my_list)}')
    mins = my_list[0]
    for i in my_list:
        if i < mins:
            mins = i
    print(mins)

create_list(6)
#Второй алгоритм:
my_list0 = [10, 20, 300, -1, -5, 1]
mins = my_list0[0]
for i in my_list0:
    if i < -1:
        print(i)

"""
Было использовано ленивое вычисление для списка.
Память обычного списка равна: 344
Память после ленивого вычисления равна: 304
"""