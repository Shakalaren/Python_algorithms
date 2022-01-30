"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from timeit import Timer


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


t1 = Timer(stmt='revers', setup="from __main__ import revers")
print("revers  ", t1.timeit(number=10000000), "seconds")


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


t2 = Timer(stmt='revers_2', setup="from __main__ import revers_2")
print("revers_2", t2.timeit(number=10000000), "seconds")


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


t3 = Timer(stmt='revers_3', setup="from __main__ import revers_3")
print("revers_3", t3.timeit(number=10000000), "seconds")


def revers_4(enter_num):
    print(f'Ваше изначальное число: {enter_num}, перевернутое: {"".join(reversed(str(enter_num)))}')


t4 = Timer(stmt='revers_4', setup="from __main__ import revers_4")
print("revers_4", t4.timeit(number=10000000), "seconds")

"""
revers   0.09125440000000001 seconds
revers_2 0.0918086 seconds
revers_3 0.08977710000000003 seconds
revers_4 0.09148300000000004 seconds
"""


"""
Функция revers_3 является наиболее эффективной по результатам замеров времени и по сложности (константная)
"""