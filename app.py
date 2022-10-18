from flask import Flask, request
import customers
import accounts
import transfers
import traceback

app = Flask(__name__)

@app.route("/")
def alive():
    response = {
        'message': "alive!!!"
    }
    return response, 200


@app.route("/customer", methods=["POST"])
def create_customer():
    return customers.create(request.json), 200


@app.route("/account/<customer_id>", methods=["POST"])
def crate_account(customer_id):
    if not request.json.get("money", False):
        return {"message": "you must specify money amount"}, 400
    return accounts.create(request.json, customer_id), 200


@app.route("/transfer", methods=["POST"])
def transfer():
    """
    payload: {"account_from": 123, "account_to": 123, "amount": 123}
    :return: {"money_left": 123}
    """
    try:
        return transfers.create(request.json), 200
    except Exception as e:
        print(traceback.format_exc()) # Here i would use a logger
        return {"message": e.args[0]}, 200



@app.route("/balances/<account_id>")
def balances(account_id):
    return {"money_left": accounts.money_left(account_id)}, 200


@app.route("/history/<account_id>")
def history(account_id):
    return transfers.history(account_id), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
