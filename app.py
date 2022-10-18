from flask import Flask, request
import customers
import accounts
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
    return accounts.create(customer_id, request.form), 200


@app.route("/transfer", methods=["POST"])
def transfer():
    """
    payload: {"account_from": 123, "account_to": 123, "amount": 123}
    :return: {"money_left": 123}
    """
    return {"money_left": 123}, 200



@app.route("/balances/<account_id>")
def balances():
    response = {
        "balance": "balance"
    }
    return response, 200


@app.route("/history/<account_id>")
def history():
    response = {
        "history": [{"tranfer":"transfer_id"}]
    }
    return response, 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
