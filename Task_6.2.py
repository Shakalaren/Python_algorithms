from json import  loads, dumps
from  pympler import asizeof
"""
Из Task 1.4
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

"""
#Было:
users = {'Andrew': {'password': 'qwerty', 'activated': 1},
         'Vlad': {'password': '123456', 'activated': 1},
         'Alex': {'password': 'zxcvb', 'activated': 0},
         'Peter': {'password': 'bnmjnh', 'activated': 0},
         'Vladimir': {'password': '456775', 'activated': 1},
         'Irene': {'password': 'vfeedd', 'activated': 0}
         }
# Решение 1: O(1)

def Authentication():
    user = input('Введите логин: ')
    CurrentUser = users.get(user)
    if not CurrentUser:
        print('Пользователь не найден')
        return False

    password = input('Введите пароль: ')
    if password != CurrentUser['password']:
        print('Пароль неверный!')
        return False

    if CurrentUser['activated'] == 0:
        input('Пользователь не активирован')
        return False
    else:
        print('Welcome!')


Authentication()


# Решение 2: O(n)

def AuthenticationCheck(users):
    user = input('Введите логин: ')
    CurrentUser = users.get(user)
    if not CurrentUser:
        print('Пользователь не зарегистрирован!')
        return False

    password = input('Введите пароль: ')
    if password != CurrentUser['password']:
        print('Пароль неверный!')
        return False

    if CurrentUser['activated'] == 0:
        activation = input('Пользователь не активирован! Введите свой логин для активации ')
        while activation != CurrentUser:
            activation = input('Ошибка, введите свой логин: ')
        else:
            CurrentUser['activated'] = 1
            print('Activation complete')
    else:
        print('Welcome!')


AuthenticationCheck(users)

# Решение 1 является более оптимальным и эффективным, так как затрачивает меньше ресурсов и времени, однако решение 2
# обладает сравнительно бОльшим функционалом и именно поэтому становится чуть более затратным.
"""
#Стало:

users = {'Andrew': {'password': 'qwerty', 'activated': 1},
         'Vlad': {'password': '123456', 'activated': 1},
         'Alex': {'password': 'zxcvb', 'activated': 0},
         'Peter': {'password': 'bnmjnh', 'activated': 0},
         'Vladimir': {'password': '456775', 'activated': 1},
         'Irene': {'password': 'vfeedd', 'activated': 0}
         }
print('Размер users: ', asizeof.asizeof(users))
dumped_dict = dumps(users)
print('Размер dumps_users: ', asizeof.asizeof(dumped_dict))

# Решение 1: O(1)

def Authentication():
    user = input('Введите логин: ')
    CurrentUser = users.get(user)
    if not CurrentUser:
        print('Пользователь не найден')
        return False

    password = input('Введите пароль: ')
    if password != CurrentUser['password']:
        print('Пароль неверный!')
        return False

    if CurrentUser['activated'] == 0:
        input('Пользователь не активирован')
        return False
    else:
        print('Welcome!')


Authentication()


# Решение 2: O(n)

def authentication_check(users):
    user = input('Введите логин: ')
    current_user = users.get(user)
    if not current_user:
        print('Пользователь не зарегистрирован!')
        return False

    password = input('Введите пароль: ')
    if password != current_user['password']:
        print('Пароль неверный!')
        return False

    if current_user['activated'] == 0:
        activation = input('Пользователь не активирован! Введите свой логин для активации ')
        while activation != current_user:
            activation = input('Ошибка, введите свой логин: ')
        else:
            current_user['activated'] = 1
            print('Activation complete')
    else:
        print('Welcome!')


authentication_check(users)

# Решение 1 является более оптимальным и эффективным, так как затрачивает меньше ресурсов и времени, однако решение 2
# обладает сравнительно бОльшим функционалом и именно поэтому становится чуть более затратным.

"""
Была использована серилизация для словаря users. Словарь сильно уменьшил свой размер после консервирования.
Размер users:  2616
Размер dumps_users:  344
"""