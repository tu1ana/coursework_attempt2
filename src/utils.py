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


