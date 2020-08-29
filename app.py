from flask import Flask
from flask import request, jsonify, render_template, redirect

from controller.payment import generate_card_token, create_payment_charge

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify("Hello world !!")

@app.route("/card", methods=["GET","POST"])
def add_card_details():
    if request.method == 'POST':
        card_number = request.form['cardnumber']
        card_expyear = request.form['expyear']
        card_expmonth = request.form['expmonth']
        card_cvv = request.form['card_cvv']

        print(card_number,card_expyear,card_expmonth,card_cvv)

        tokenid = generate_card_token(card_number,card_expmonth,card_expyear,card_cvv)

        payment_done = create_payment_charge(tokenid,40)

        return jsonify({"success":payment_done})

    else:
        return render_template("payment.html")






if __name__ == "__main__":
    app.run()