#! usr/bin/python3
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key= "alien"



@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html', counter = session["counter"])

@app.route('/clear')
def clear():
    session['counter'] = 0
    return redirect('/')

@app.route('/two')
def two():
    session['counter'] += 1
    return redirect('/')



if __name__ == '__main__':
    app.run(debug= True, port = 2020)
