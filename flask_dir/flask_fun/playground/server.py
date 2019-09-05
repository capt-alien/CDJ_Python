#!python3
from flask import Flask, render_template

app=Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html")


@app.route('/play/<num>/<color>')
def play(num, color):
    times = int(num)
    print("TEST")
    return render_template("game.html", num=times, color=color)



if __name__=="__main__":
    app.run(debug=True)
