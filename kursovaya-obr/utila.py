import json
from datetime import datetime


def loading_json(file_json):
    """
    Функция загружает данные из файла operations.json
    :param file_json:
    :return: выводит список словарей
    """
    with open(file_json, "r") as file:
        return json.load(file)


def get_list_sorted(file):
    """
    Функция которая находит в файле operations.json пустой словарь и отсортировывает статус 'EXECUTED'
    :param file: подается файл который получается в результате функции loading_json(file_json)
    :return: список словарей со статусами операций 'EXECUTED'
    """
    json_selection = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', file))
    return json_selection


def sorts_date(json_selection):
    """
    Функция которая сортирует списко словарей json_selection по дате на убывание (с верху самая крайняя дата)
    :param json_selection: список полученный в результате вызова функции get_list_sorted(file)
    :return: отсортерованный список по дате (Сверху списка находятся самые последние операции (по дате))
    """
    json_sort = sorted(json_selection,key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return json_sort


def get_date(date):
    """
    Функция которая выдает дату операции
    :param date: дада из файла operratuons.json
    :return: дату в формате 14.10.2018
    """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


