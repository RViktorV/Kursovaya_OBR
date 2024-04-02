import json
def loading_json(file_json):
    """
    Функция загружает данные из файла operations.json
    :param file_json:
    :return:
    """
    with open(file_json, "r") as file:
        return json.load(file)


def get_list_sorted(file):
    json_selection = list(filter(lambda a: len(a) and a['stse'] == 'EXECUTED', file))
    return json_selection

print(get_list_sorted(loading_json('operations.json')))