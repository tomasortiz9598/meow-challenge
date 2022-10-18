import helpers
from exceptions import InvalidIdException, NotEnoughMoneyException



def create(payload, customer_id):
    payload.update({"customer_id": customer_id})
    return helpers.save("accounts", payload)  # here i would use a database that returns me the id


def get(account_id):
    accounts = helpers.get("accounts")
    print(accounts)
    for account in accounts:
        if account["id"] == account_id:
            return account
    raise InvalidIdException("")


def money_left(account_id):
    print(get(account_id))
    return get(account_id)["money"]


def add_money(account_id, money):
    account = helpers.get_by_id("accounts", account_id)
    helpers.update("accounts", account_id, {"money": account["money"] + money})


def discount_money(account_id, money):
    print(money)
    print(money_left(account_id))
    if money_left(account_id) < money:
        raise NotEnoughMoneyException("You don't have enough money")

    account = helpers.get_by_id("accounts", account_id)
    helpers.update("accounts", account_id, {"money": account["money"] - money})

