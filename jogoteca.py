# _*_ encoding: utf-8 _*_

from flask import Flask

app = Flask(__name__)


@app.route("/initial")
def hello():
    """ This is just a simple sample! Never mix HTML at this part of your code. """
    return "<h1>Hello from Flask App!"


app.run()

