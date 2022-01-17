"""
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

users = {'Andrew': {'password': 'qwerty', 'activated': 1},
         'Vlad': {'password': '123456', 'activated': 1},
         'Alex': {'password': 'zxcvb', 'activated': 0},
         'Peter': {'password': 'bnmjnh', 'activated': 0},
         'Vladimir': {'password': '456775', 'activated': 1},
         'Irene': {'password': 'vfeedd', 'activated': 0}
         }


# Решение 1: O(1)

def authentication():
    user = input('Введите логин: ')
    current_user = users.get(user)
    if not current_user:
        print('Пользователь не найден')
        return False

    password = input('Введите пароль: ')
    if password != current_user['password']:
        print('Пароль неверный!')
        return False

    if current_user['activated'] == 0:
        print('Пользователь не активирован')
        return False
    else:
        print('Welcome!')


authentication()


# Решение 2: O(n)

def authentication_check():
    user_check = []
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
        print('Пользователь не активирован! Пожалуйста, пройдите верификацию')
        for i in user: #O(n)
            user_check.append(i)
        activation = input('Напишите любую букву, которая есть в Вашем логине: ')
        while activation not in user_check:
            activation = input('Напишите любую букву, которая есть в Вашем логине: ')
        else:
            current_user['activated'] = 1
            print('Activation complete')
    else:
        print('Welcome!')


authentication_check()


# Решение 1 является более оптимальным и эффективным, так как затрачивает меньше ресурсов и времени, однако решение 2
# обладает сравнительно бОльшим функционалом и именно поэтому становится чуть более затратным.
