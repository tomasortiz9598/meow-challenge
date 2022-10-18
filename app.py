from flask import Flask
app = Flask(__name__)

@app.route("/alive")
def alive():
    response = {
        'message': "alive!!!"
    }
    return response, 200


@app.route("/customer", methods=["POST"])
def create_customer():
    #create_customer()
    return {"customer_id": ""}, 200


@app.route("/account/<customer_id>", methods=["POST"])
def crate_account():
    return {"account_id": ""}, 200


@app.route("/transfer", methods=["POST"])
def transfer():
    '''
    payload: {"account_from": 123, "account_to": 123, "amount": 123}
    :return:
    '''
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
