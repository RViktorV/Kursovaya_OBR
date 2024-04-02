import json
def loading_json(file_json):
    """
    Функция загружает данные из файла operations.json
    :param file_json:
    :return:
    """
    with (open(file_json, 'r') as file:
        return  json.load(file)


