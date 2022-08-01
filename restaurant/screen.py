from .management import get_item, add_item_to_tab, calculate_tab

from datetime import date, time, datetime, timedelta, timezone

from utils.json_handler import read_json, write_json

import os

FILEPATH = 'menu.json'

table_handler = []

os.system('clear')


def initial_screen():
    continue_looping = True

    data = read_json(FILEPATH)
    new_item = {"id":35, "name": "CHURROS DO M5", "price": 5.0}
    data.append(new_item)
    write_json(FILEPATH, data)

    print('Bem vindo ao restaurante da Kenzie!')
    print('-' * 50)
    print('-' * 50)

    while continue_looping:
        print('Escolha entre uma das opções abaixo:')
        print('1 - Adicionar item ao pedido')
        print('2 - Calcular total do pedido')

        option = input('Digite a opção desejada: ')

        if option == '1':
            print('-' * 50)
            print('Items disponíveis:')
            print(data)
            print('-' * 50)
            add_item_screen()
        elif option == '2':
            continue_looping = False
            check_out_screen()
        else:
            os.system('clear')
            print('Opção inválida!')


def add_item_screen():
    is_adding_item = False
    print('-' * 50)
    while not is_adding_item:
        item_id = input('Digite o id do item: ')
        amount = input('Digite a quantidade do item: ')

        adding_item = add_item_to_tab(table_handler, int(item_id), int(amount))

        if adding_item:
            os.system('clear')

            for item in table_handler:
                print(
                    f'{item["amount"]} {item["name"]} adicionado(s) a comanda!\n')

            is_adding_item = True

        else:
            os.system('clear')
            print('Item não encontrado!')


def check_out_screen():
    os.system('clear')

    STR_FORMAT = '%d/%m/%y %H:%M:%S'
    closing_commands = datetime.now()

    total_price = 0
    quit = False

    for item in table_handler:
        total_price += item['price']*item['amount']

    while not quit:
        os.system('clear')
        for index, item in enumerate(table_handler):
            print(
                f'Item {index + 1}: {item["amount"]} {item["name"]} - R$ {item["price"] * item["amount"]}')

        print('-' * 50)
        print(f'SUBTOTAL: R${total_price}')
        print(
            f'DATA DO FECHAMENTO DA COMANDA: {closing_commands.strftime(STR_FORMAT)}')
        exit = input('Digite F para sair do sistema')

        if exit.upper() == 'F':
            quit = True