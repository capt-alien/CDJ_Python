#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
from glob import glob

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print("*"*50)
    total =(int(request.form["strawberry"])+int(request.form["raspberry"])+int(request.form["apple"]))
    print(request.form)
    return render_template("checkout.html", strawberry=request.form["strawberry"], raspberry=request.form["raspberry"], apple=request.form["apple"], first_name=request.form["first_name"], last_name=request.form["last_name"], student_id=request.form["student_id"], total= total)


@app.route('/fruits')
def fruits():
    p_list = glob.glob("static/img/*")
    photos_list = []
    for p in p_list:
        p = p[11::]
        photos_list.append(p)
    return render_template("fruits.html", photos=photos_list)

if __name__=="__main__":
    app.run(debug=True)
