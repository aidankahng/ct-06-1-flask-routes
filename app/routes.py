from flask import request, render_template
from app import app

user_inputs = [""]


@app.route("/index")
def display_homepage():
    return """
This is a webpage
I could put html elements in here...
Wow
"""


@app.route("/blackjack")
def play_blackjack():
    return """
If I completed this page you would be able to play blackjack here...
"""


@app.route("/blackjack/hiscores")
def display_hiscores():
    return """
Highscores:
Name : Score
Name : Score
Your Name: Your Score
"""

@app.route('/repeat', methods=["GET"])
def repeat_form():
    return render_template("form.html")

@app.route('/repeat', methods =["POST"])
def repeat():
    user_inputs = []
    # get user input from the html webpage
    user_input = request.form.get("test_input")
    if user_input == "reset":
        user_inputs = [""]
    elif user_input != "":
        user_inputs.append(user_input)
    else:
        user_inputs.append(" Empty ")
    return render_template("form.html") + f"{"<br>".join([i for i in user_inputs])}"