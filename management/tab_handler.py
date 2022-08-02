from utils.json_handler import read_json, write_json

table_handler = list()

FILEPATH = 'menu.json'

def get_item(item_id: int) -> dict:
    for item in read_json(FILEPATH):
        if item['id'] == item_id:
            return item

    return None


def add_item_to_tab(table_handler: list, item_id: int, amount: int) -> bool:
    item = get_item(item_id)

    if not item:
        return False

    table_handler.append(
        dict(id=item['id'], name=item['name'], price=item['price'], amount=amount))

    return True


def calculate_tab(table_handler: list) -> int:
    total = 0

    for item in table_handler:
        total += item['price'] * item['amount']

    return total