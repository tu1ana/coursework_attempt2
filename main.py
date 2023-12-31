from src.utils import load_operations, get_exec_transaction, get_last_transactions, display_data

last_transactions = 5


def main():
    init_list = load_operations()
    sorted_list = get_exec_transaction(init_list)
    data = get_last_transactions(sorted_list, last_transactions)
    data = display_data(data)

    for line in data:
        print(line, end='\n\n')


if __name__ == '__main__':
    main()
