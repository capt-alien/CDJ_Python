#!python3

from flask import Flask

app = Flask(__name__)

# routes
@app.route('/')
def hello_world():
    return "Hello World"

#Dojo
@app.route('/dojo')
def dojo():
    return "DOJO!!!"

#say
@app.route('/say/<name>')
def say(name):
    return "Hi " + name + "!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    word =word+" "
    num = int(num)
    return num*word




if __name__ == '__main__':
    app.run(debug= "True")
