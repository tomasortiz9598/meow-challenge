import db
from exceptions import InvalidIdException, NotEnoughMoneyException, InvalidArgumentException
from validators import validate_input


def create(payload, customer_id):
    validate_input(payload, ["money"])
    payload.update({"customer_id": customer_id})
    return db.save("accounts", payload)  # here i would use a database that returns me the id


def get(account_id):
    for account in db.get("accounts"):
        if account["id"] == account_id:
            return account
    raise InvalidIdException("")


def money_left(account_id):
    return get(account_id)["money"]


def add_money(account_id, money):
    account = db.get_by_id("accounts", account_id)
    db.update("accounts", account_id, {"money": account["money"] + money})


def discount_money(account_id, money):
    if money_left(account_id) < money:
        raise NotEnoughMoneyException("You don't have enough money")

    account = db.get_by_id("accounts", account_id)
    db.update("accounts", account_id, {"money": account["money"] - money})
