import json

def read_json(filepath: str) -> list[dict]:
    with open(filepath, 'r') as file:
        return json.load(file)

def write_json(filepath: str, payload: list[dict]):
    with open(filepath, 'w') as file:
        json.dump(payload, file, indent=2)