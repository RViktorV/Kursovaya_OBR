import os
from config import ROOT_DIR
from kursovaya_obr.utils import loading_json, get_list_sorted

def test_loading_json():
    TEST_PATH = os.path.join(ROOT_DIR, 'tests', 'test.json')
    assert loading_json(TEST_PATH) == [1, 2, 3, 4]


def teat_get_list_sorted():
    TEST_FILE = os.path.join(ROOT_DIR, 'tests', 'test.txt')
    assert get_list_sorted(TEST_FILE) == [
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