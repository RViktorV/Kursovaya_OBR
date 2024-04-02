import json
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
    функция которая находит в файле operations.json пустой словарь и отсортировывает статус 'EXECUTED'
    :param file: подается файл который получается в результате функции loading_json(file_json)
    :return: список словарей со статусами операций 'EXECUTED'
    """
    json_selection = list(filter(lambda a: len(a) and a['state'] == 'EXECUTED', file))
    return json_selection

