from flask import Flask
from flask import request, jsonify, render_template, redirect

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("payment.html")







if __name__ == "__main__":
    app.run()