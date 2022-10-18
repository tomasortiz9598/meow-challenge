from db import save


def create(payload):
    return save("customers", payload)
