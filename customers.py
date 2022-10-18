from helpers import save


def create(payload):
    return save("customers", payload) #here i would use a database that returns me the id
