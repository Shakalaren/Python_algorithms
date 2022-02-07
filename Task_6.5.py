"""
Из Task_5.2. Идентичный код заключен в комментарии. 
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
from pympler import asizeof
#Было:
"""
#Способ через defaultdict

from collections import defaultdict

num_1 = input('Введите шестандацатиричное число, например (А2): ')
num_2 = input('Введите шестандацатиричное число, например (C4F): ')

my_dict = defaultdict(list)


def create_dict(x):
    for i in x:
        my_dict[x].append(i)


create_dict(num_1)
create_dict(num_2)

def get_sum(x, y):
    result = hex(int(x, 16) + int(y, 16))[2:].upper()
    if result not in my_dict:
        for i in result:
            my_dict[result].append(i)
    return result


print(f'Сумма чисел {num_1} и {num_2} равна: {get_sum(num_1, num_2)}')


def get_mul(x, y):
    result = hex(int(x, 16) * int(y, 16))[2:].upper()
    if result not in my_dict:
        for i in result:
            my_dict[result].append(i)
    return result


print(f'Произведение чисел {num_1} и {num_2} равно: {get_mul(num_1, num_2)}')

"""
#Способ через ООП
num_1 = input('Введите шестандацатиричное число, например (А2): ')
num_2 = input('Введите шестандацатиричное число, например (C4F): ')

class HexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return hex(int(self.num_1, 16) + int(self.num_2, 16))[2:].upper()

    def __mul__(self, other):
        return hex(int(self.num_1, 16) * int(self.num_2, 16))[2:].upper()

HN_OBJECT = HexNumber(num_1, num_2)
print(f'Размер без слотов слотами: {asizeof.asizeof(HN_OBJECT)}')
print(f'Сумма чисел {num_1} и {num_2} равна: {HexNumber(num_1, num_2) + HexNumber(num_1, num_2)}')
print(f'Произведение чисел {num_1} и {num_2} равно: {HexNumber(num_1, num_2) * HexNumber(num_1, num_2)}')


#Стало
"""
#Способ через defaultdict

from collections import defaultdict

num_1 = input('Введите шестандацатиричное число, например (А2): ')
num_2 = input('Введите шестандацатиричное число, например (C4F): ')

my_dict = defaultdict(list)


def create_dict(x):
    for i in x:
        my_dict[x].append(i)


create_dict(num_1)
create_dict(num_2)

def get_sum(x, y):
    result = hex(int(x, 16) + int(y, 16))[2:].upper()
    if result not in my_dict:
        for i in result:
            my_dict[result].append(i)
    return result


print(f'Сумма чисел {num_1} и {num_2} равна: {get_sum(num_1, num_2)}')


def get_mul(x, y):
    result = hex(int(x, 16) * int(y, 16))[2:].upper()
    if result not in my_dict:
        for i in result:
            my_dict[result].append(i)
    return result


print(f'Произведение чисел {num_1} и {num_2} равно: {get_mul(num_1, num_2)}')

"""
num_1 = input('Введите шестандацатиричное число, например (А2): ')
num_2 = input('Введите шестандацатиричное число, например (C4F): ')

class HexNumber0:
    __slots__ = ['num_1', 'num_2']

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return hex(int(self.num_1, 16) + int(self.num_2, 16))[2:].upper()

    def __mul__(self, other):
        return hex(int(self.num_1, 16) * int(self.num_2, 16))[2:].upper()

HN_OBJECT0 = HexNumber0(num_1, num_2)
print(f'Размер со слотами: {asizeof.asizeof(HN_OBJECT0)}')
print(f'Сумма чисел {num_1} и {num_2} равна: {HexNumber(num_1, num_2) + HexNumber(num_1, num_2)}')
print(f'Произведение чисел {num_1} и {num_2} равно: {HexNumber(num_1, num_2) * HexNumber(num_1, num_2)}')

"""
Вариант с использованием слотов в ООП.
Размер без слотов слотами: 376
Размер со слотами: 160
"""