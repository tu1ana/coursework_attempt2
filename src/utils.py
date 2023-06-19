import json


def load_operations():
    with open('operations.json', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def get_exec_transaction(list_):
    sorted_list = [x for x in list_ if 'state' in x and x['state'] == 'EXECUTED']
    return sorted_list
