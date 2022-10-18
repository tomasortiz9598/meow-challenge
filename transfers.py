import json

from helpers import save, get
from exceptions import InvalidArgumentException, NotEnoughMoneyException
from accounts import money_left, add_money, discount_money


def create(payload):
    requested_params = ["account_from", "account_to", "amount"]
    for requested_param in requested_params:
        if not payload.get(requested_param, False):
            raise InvalidArgumentException("you must specify {}".format(requested_param))

    discount_money(payload.get("account_from"), payload.get("amount"))

    add_money(payload.get("account_to"), payload.get("amount"))

    return save("transfers", payload)


def history(account_id):
    return {"result": list(filter(lambda x: x["account_from"] == account_id, get("transfers")))}
