from db import save, get
from accounts import add_money, discount_money
from validators import validate_input


def create(payload: dict) -> dict:
    validate_input(payload, ["account_from", "account_to", "amount"])

    discount_money(payload.get("account_from"), payload.get("amount"))

    add_money(payload.get("account_to"), payload.get("amount"))

    return save("transfers", payload)


def history(account_id: str) -> dict:
    return {"result": list(filter(lambda x: x["account_from"] == account_id, get("transfers")))}
