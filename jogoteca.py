# _*_ encoding: utf-8 _*_

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/initial")
def hello():
    return render_template("games.html", title="Games")


"""
    If necessary we can define host and port for our server.
    e.g app.run(host="127.0.0.1", port=5001)
"""
app.run()

