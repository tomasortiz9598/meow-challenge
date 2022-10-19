from db import save


def create(payload: dict) -> dict:
    return save("customers", payload)
