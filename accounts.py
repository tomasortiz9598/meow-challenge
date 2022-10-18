from helpers import save

def create(payload, customer_id):
    save("accounts", {"customer_id": customer_id,
                      "account": payload}) #here i would use a database that returns me the id
    return {"account_id": ""}