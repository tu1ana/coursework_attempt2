import pytest
from src.utils import load_operations, get_exec_transaction, get_last_transactions, encode_data, display_data


def test_load_operations():
    data = load_operations()
    assert isinstance(data, list)


def test_get_exec_transaction(test_data):
    data = get_exec_transaction(test_data)
    assert len(data) == 3


def test_get_last_transactions(test_data):
    data = get_last_transactions(test_data, 6)
    assert [x['date'] for x in data] == ["2019-07-15T11:47:40.496961", "2019-07-13T18:51:29.313309", "2019-05-19T12:51:49.023880", "2019-01-05T00:52:30.108534", "2018-12-24T20:16:18.819037", "2018-03-09T23:57:37.537412"]


@pytest.mark.parametrize('test_input, expected', [
    ("МИР 5211277418228469", "МИР 5211 27** **** 8469"),
    ("Счет 58518872592028002662", "Счет **2662")
])
def test_encode_data(test_input, expected):
    assert encode_data(test_input) == expected


def test_display_data(test_data):
    data = display_data(test_data)
    assert data == ['19.05.2019 Перевод организации\nМИР 5211 27** **** 8469 -> Счет **2662\n6381.58 USD', '24.12.2018 Перевод со счета на счет\nСчет **5290 -> Счет **9781\n991.49 руб.', '09.03.2018 Перевод организации\nСчет **3262 -> Счет **1315\n25780.71 руб.', '15.07.2019 Открытие вклада\nСчет **2265\n92688.46 USD', '05.01.2019 Перевод со счета на счет\nСчет **8409 -> Счет **8266\n87941.37 руб.', '13.07.2019 Перевод с карты на счет\nMaestro 1308 79** **** 7170 -> Счет **8612\n97853.86 руб.']
