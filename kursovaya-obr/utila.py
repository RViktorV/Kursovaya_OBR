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
    :return: дата в формате 14.10.2018
    """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


def get_num_carte(num):
    """
    Функция которая шифрует номер счета или номер карты по которой проводится транзакция
    :param num: номер карты или счета
    :return:будет наименоваине карты(или счет) и зашифрованный ее номер
    """
    data_cart = num.split()
    if data_cart[0] == "Счет":
        return f"Счет **" + num[-4:]
    else:
        cart_name = " ".join(data_cart[:-1])
        return f"{cart_name} {data_cart[-1][4:6]} •• •••• {data_cart[-1][-4:]}"


def get_converted_amount(cash):
    """
    Функция выводит количство денег по операции и нименование валюты
    :param cash: сумма переведенная по транзакции
    :return:выводит сумму и в какой валюете
    """
    return f"{cash['operationAmount']["amount"]} {cash['operationAmount']["currency"]["name"]}"


def main(numbers_operations=5):
    """
    Функция которая выводит на экран список из 5 последних выполненных клиентом операций в формате:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    """
    file_json = loading_json('operations.json')
    sorting_operation = get_list_sorted(file_json)
    sort_by_data = sorts_date(sorting_operation)
    for operation in sort_by_data:
        if numbers_operations == 0:
            break
        print(get_date(operation['date']), operation['description'])
        if operation['description'] != "Открытие вклада":
            print(get_num_carte(operation['from'])+' -> ', end='')
        print(get_num_carte(operation['to']))
        print(get_converted_amount(operation),'\n')
        numbers_operations -= 1




