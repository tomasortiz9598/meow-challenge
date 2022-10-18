from helpers import save


def create(payload):
    print(payload)
    save("customers", payload) #here i would use a database that returns me the id
    return {"customer_id": ""}
