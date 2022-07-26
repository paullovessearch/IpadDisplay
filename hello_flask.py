from flask import Flask
app = Flask(__name__)

@app.route("/hello/<what>")
def hello(what):
    return "Hello " + what + "!"

@app.route("/hola")
def hola():
    return "Hola, Mundo!!"
