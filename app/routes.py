from flask import request
from app import app

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