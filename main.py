import random, json

from datetime import datetime
from operator import itemgetter
from flask import Flask, render_template, request, make_response


# Flask runtime
app = Flask(__name__)


# index page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("welcome.html")
    elif request.method == "POST":
        return render_template("welcome.html")


# game page and game routine
@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        if not request.cookies.get("secret_number"):
            print("No cookie")
            response = make_response(render_template("game.html"))
            response.set_cookie("secret_number", str(random.randint(1, 30)))
            return response

        else:
            return render_template("game.html")

    elif request.method == "POST":
        try:
            guess = int(request.form.get("guess"))
        except ValueError:
            return render_template("game.html", no_int=True)

        if guess < int(request.cookies.get("secret_number")):
            helpline = "Your guess is below the secret number."
        elif guess > int(request.cookies.get("secret_number")):
            helpline = "Your guess is above the secret number."
        else:
            helpline = "Hooray"

        return render_template("game.html", helpline=helpline)


# main routine to start the app
if __name__ == "__main__":
    app.run(debug=True)
