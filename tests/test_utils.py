import os
from config import ROOT_DIR
from kursovaya_obr.utils import loading_json, get_list_sorted, sorts_date, get_date, get_num_carte, get_converted_amount, main

def test_loading_json():
    TEST_PATH = os.path.join(ROOT_DIR, 'tests', 'test.json')
    assert loading_json(TEST_PATH) == [1, 2, 3, 4]

test_executed = [
 {
     "id": 441945886,
     "state": "EXECUTED",
     "date": "2019-08-26T10:50:58.294041"
 },
 {},
 {
     "id": 441945887,
     "state": "EXECUTED",
     "date": "2019-10-26T10:50:58.294042"
 },
]

def test_get_list_sorted():
    assert get_list_sorted(test_executed) == [
 {
     "id": 441945886,
     "state": "EXECUTED",
     "date": "2019-08-26T10:50:58.294041"
 },
 {
     "id": 441945887,
     "state": "EXECUTED",
     "date": "2019-10-26T10:50:58.294042"
 },
]

test_date = [
{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"
    },
    {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
    }

]


def test_sorts_date():
    assert sorts_date(test_date) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
    },
    {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"
    }
]


def test_get_date():
    assert get_date("2019-07-03T18:35:29.512364") == '03.07.2019'


def test_get_num_carte():
    assert get_num_carte("Maestro 1596837868705199") == 'Maestro 83 •• •••• 5199'
    assert get_num_carte("Счет 64686473678894779589") == 'Счет **9589'


def test_get_converted_amount():
    assert get_converted_amount({
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }) == '48223.05 руб.'


