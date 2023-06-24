import json
from datetime import datetime
from operator import itemgetter


def load_operations():
    """Загружает данные по операциям"""
    with open('operations.json', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def get_exec_transaction(list_: list):
    """Сортирует данные, возвращает список только выполненных операций"""
    sorted_list = [x for x in list_ if 'state' in x and x['state'] == 'EXECUTED']
    return sorted_list


def get_last_transactions(list_: list, last_transactions: int):
    """Сортирует список по дате"""
    sorted_list = sorted(list_, key=itemgetter('date'), reverse=True)
    sorted_list = sorted_list[:last_transactions]
    return sorted_list


def encode_data(bill_info: str):
    """Зашифровывает платёжные данные"""
    bill_info = bill_info.split()
    bill = bill_info[-1]
    info = ' '.join(bill_info[:-1])
    if len(bill) == 16:
        bill = f'{bill[:4]} {bill[4:6]}** **** {bill[-4:]}'
    else:
        bill = f'**{bill[-4:]}'

    to = f'{info} {bill}'
    return to


def display_data(list_: list):
    """Выводит информацию по операциям следующего вида:
    '14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.'"""
    formatted_data = []
    for el in list_:
        date_obj = datetime.strptime(el['date'], '%Y-%m-%dT%H:%M:%S.%f')
        new_date = date_obj.strftime('%d.%m.%Y')

        description = el['description']

        if 'from' in el:
            sender = encode_data(el['from'])
            sender = f'{sender} -> '
        else:
            sender = ''

        to = encode_data(el['to'])
        operation_amt = f"{el['operationAmount']['amount']} {el['operationAmount']['currency']['name']}"

        formatted_data.append((f'''\
{new_date} {description}
{sender}{to}
{operation_amt}'''))
    return formatted_data
