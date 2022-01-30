"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""


from collections import namedtuple


def company_check():
    storage = []
    setup = namedtuple('Company', "name quarter_1 quarter_2 quarter_3 quarter_4")

    for i in range(int(input('Введите количество предприятий: '))):
        name = input('Введите название предприятия: ')
        quarter_1 = int(input('Введите прибыль за первый квартал: '))
        quarter_2 = int(input('Введите прибыль за второй квартал: '))
        quarter_3 = int(input('Введите прибыль за третий квартал: '))
        quarter_4 = int(input('Введите прибыль за четвертый квартал: '))
        company = setup(
            name=name,
            quarter_1=quarter_1,
            quarter_2=quarter_2,
            quarter_3=quarter_3,
            quarter_4=quarter_4
        )
        storage.append(company)
    total_average = sum(map(lambda x: x.quarter_1 + x.quarter_2 + x.quarter_3 + x.quarter_4, storage)) / len(storage)
    print(f'Средняя прибыль всех компаний за весь год: {total_average}')

    above_average = []
    below_average = []
    for company in storage:
        company_profit = company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4
        if company_profit > total_average:
            above_average.append(company.name)
        elif company_profit < total_average:
            below_average.append(company.name)
    print(f'Компании, с прибылью выше среднего значения: {above_average}')
    print(f'Компании, с прибылью ниже среднего значения: {below_average}')


company_check()