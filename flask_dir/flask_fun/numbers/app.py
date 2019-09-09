#! usr/bin/python3
from flask import Flask, render_template, request, redirect, session
from random import randint


app = Flask(__name__)
app.secret_key= "alien"
# session["status"] = "first"




@app.route('/')
def index():
    # declare random in session if not existing
    if "random" not in session:
        session["random"]= randint(1,100)
        print("*"*50)
        print(session["random"])
        session["status"]= "first"
        print("*"*50)
        print(session["status"])
    else:
        print("*"*50)
        print(session["status"])
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    guess = int(request.form["guess"])
    print(guess)
    if guess == session["random"]:
        session["status"] = "won"
    elif guess > session["random"]:
        session["status"] = "high"
    else:
        session["status"] = "low"
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session["random"]= randint(1,100)
    session['status']="first"
    return redirect('/')




if __name__ == '__main__':
    app.run(debug= True, port = 2020)
