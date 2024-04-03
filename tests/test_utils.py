import os
from config import ROOT_DIR
from kursovaya_obr.utils import loading_json

def test_loading_json():
    TEST_PATH = os.path.join(ROOT_DIR, 'tests', 'test.json')
    assert loading_json(TEST_PATH) == [1, 2, 3, 4]