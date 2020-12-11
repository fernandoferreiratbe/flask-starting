# _*_ encoding: utf-8 _*_

from flask import Flask, render_template


class Game:

    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

    def __str__(self):
        return f"Name -> {self.name} - Category -> {self.category} - Console -> {self.console}"


app = Flask(__name__)


@app.route('/initial')
def hello():
    game1 = Game('Super Mario', 'Action', 'SNT')
    game2 = Game('Pokemon Gold', 'RPG', 'GBA')
    games = [game1, game2]

    return render_template("games.html", title="Games", games=games)


@app.route('/new')
def create_new_game():
    title = 'Games'
    return render_template('new_game.html', title=title)


"""
    If necessary we can define host and port for our server.
    e.g app.run(host="127.0.0.1", port=5001)
"""
app.run()

