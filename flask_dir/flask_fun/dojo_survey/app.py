#!python3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


#midleware
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def save_survey():
    print("*"*50)
    print(request.form)

    return render_template('result.html',name=request.form["name"], location=request.form["location"], language=request.form['language'], comment=request.form('comment') )


# @app.route('/result')
# def result():
#     return render_template('result.html')
#



#bottomware
if __name__ == '__main__':
    app.run(debug=True, port=2020)
