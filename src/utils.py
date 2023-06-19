import json
from operator import itemgetter


def load_operations():
    with open('operations.json', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def get_exec_transaction(list_):
    sorted_list = [x for x in list_ if 'state' in x and x['state'] == 'EXECUTED']
    return sorted_list


def get_last_transactions(list_, last_transactions):
    sorted_list = sorted(list_, key=itemgetter('date'), reverse=True)
    sorted_list = sorted_list[:last_transactions]
    return sorted_list


def encode_data(bill_info):
    bill_info = bill_info.split()
    bill = bill_info[-1]
    info = ' '.join(bill_info[:-1])
    if len(bill) == 16:
        bill = f'{bill[:4]} {bill[4:6]}** ****{bill[-4:]}'
    else:
        bill = f'**{bill[-4:]}'

    to = f'{info} {bill}'
    return to


