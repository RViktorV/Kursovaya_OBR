import os
from config import ROOT_DIR
from kursovaya_obr.utils import loading_json, get_list_sorted, sorts_date

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

