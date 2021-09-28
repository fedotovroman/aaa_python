#-------------------------------------------------------------------------------
# Name:        Report Generator
# Purpose:
#
# Author:      Roman
#
# Created:     28.09.2021
# Copyright:   (c) Roman Fedotov 2021
#-------------------------------------------------------------------------------

import csv

def workers_dict()-> list:
    """
    Открывает csv-файл Corp_Summary и возвращает лист с
    элементами в виде словарей, содержащих информацию о сотрудниках компании.

    Parameters
    ----------
    Без параметров

    Returns
    -------
    Лист с элементами в виде словарей, содержащих
    информацию о сотрудниках компании.

    """
    workers = []
    with open('Corp_Summary.csv', newline='',encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            workers.append(row)
    return workers


def get_departments(workers: list) -> list:
    """
    Возвращает список департаментов

    Parameters
    ----------
    workers: list
        лист с элементами в виде словарей, содержащих
        информацию о сотрудниках компании.

    Returns
    -------
    departments: list
        список существующих департаментов в отчете
    """
    departments = []
    for worker in workers:
        if worker['Департамент'] not in departments:
            departments.append(worker['Департамент'])
    return departments

def get_report(workers: list) -> dict:

    """
    Отображает иерархию департаментов и отделов в компании

    Parameters
    ----------
    workers : list
        лист с элементами в виде словарей, содержащих
        информацию о сотрудниках компании.

    Returns
    -------
    report: dict
        словарь департаментов, ассоциированных с отчетом о
        данном департаменте
    """
    report = dict()
    departments = get_departments(workers)
    for dep in departments:
        salaries = []
        for worker in workers:
            if worker['Департамент'] == dep:
                salaries.append(int(worker['Оклад']))
        report[dep] =[len(salaries),  f'{min(salaries)} -- {max(salaries)}',round(sum(salaries)/len(salaries),2)]
    return report


def show_hierarchy(report: dict):
    """
    Отображает иерархию департаментов и отделов в компании

    Parameters
    ----------
    report: dict
        словарь департаментов, ассоциированных с отчетом о
        данном департаменте

    Returns
    -------
        консольное иерархическое представление департаментов
        и отделов в компании
    """

    workers = workers_dict()
    hierarchy = dict()
    for worker in workers:
        if worker['Отдел'] not in hierarchy.get(worker['Департамент'],[]):
            hierarchy.setdefault(worker['Департамент'], []).append(worker['Отдел'])
    print('Иерархия команд\n')
    for dep in hierarchy.keys():
        print(f'├─{dep}')
        for com in hierarchy[dep]:
            print(f'|  {com}')
        print()




def show_report(report: dict):
    """
    Отображает сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату

    Parameters
    ----------
    report: dict
        словарь департаментов, ассоциированных с отчетом о
        данном департаменте

    Returns
    -------
    Консольное представление сводного отчёта по департаментам:
    название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату
    """

    print('Сводный отчет по департаментам \n')
    for dep in report.keys():
        print(f'├─{dep}')
        print(f'| Число сотрудников: {report[dep][0]} человек ')
        print(f'| Вилка зарплат: {report[dep][1]} руб. ')
        print(f'| Средняя зарплата: {report[dep][2]} руб. \n')

def report_to_csv(report: dict):
    """
    Создает в исходной папке скрипта файл Report_Dep.csv, содержащий
    сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату

    Parameters
    ----------
    report: dict
        словарь департаментов, ассоциированных с отчетом о
        данном департаменте

    Returns
    -------
    Консольный отчет об успешном создании файла и файл Report_Dep.csv
    """
    with open('Report_Dep.csv', 'w', newline = '',encoding='cp1251') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';')
        filewriter.writerow(['Название департамента','Число сотрудников','Вилка зарплат','Средняя зарплата'])
        for dep in report.keys():
            filewriter.writerow(([dep]+report[dep]))
    print('Файл Report_Dep.csv успешно создан.')

def main():
    """
    Главный метод программы, является интерфейсом пользователя

    """
    print('ООО "Рога и Копыта" \n')
    options = {1: show_hierarchy, 2: show_report, 3:report_to_csv}
    option = 0
    while option not in options:
        print('Пожалуйста, выберете номер нужной опции:')
        print(
        '1. Вывести иерархию команд \n'
        '2. Вывести сводный отчёт по департаментам \n'
        '3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла \n'
        )
        option = int(input('Нужная опция: '))
    print()
    options[option](get_report(workers_dict()))
    input("Нажмите любую кнопку, чтобы выйти ...")

if __name__ == '__main__':
    main()
