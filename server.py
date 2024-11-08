from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1> \
            <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='A gif that shows number between 0 and 9.'/>"

def random_number():
    return random.randint(0, 9)

@app.route("/<int:number>")
def guess(number):
    if number == random_number():
        return "<h1 style='color: green; font-weight: bold'>You found me!</h1> \
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif number < random_number():
        return "<h1 style='color: red; font-weight: bold'>Too low, try again!</h1> \
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif number > random_number():
        return "<h1 style='color: purple; font-weight: bold'>Too high, try again!</h1> \
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)