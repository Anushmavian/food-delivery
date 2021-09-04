import json


def create_id(payload):
    with open('order.json', 'w') as fp:
        json.dump(payload, fp)
