# _*_ encoding: utf-8 _*_

from flask import Flask, render_template, request


class Game:

    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

    def __str__(self):
        return f"Name -> {self.name} - Category -> {self.category} - Console -> {self.console}"


page_title = "Games"
game1 = Game('Super Mario', 'Action', 'SNT')
game2 = Game('Pokemon Gold', 'RPG', 'GBA')
games = [game1, game2]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("games.html", title=page_title, games=games)


@app.route('/new')
def new_game():
    return render_template('new_game.html', title=page_title)


@app.route('/create_game', methods=['POST', ])
def create_game():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    games.append(Game(name, category, console))

    return render_template('games.html', title=page_title, games=games)


"""
    If necessary we can define host and port for our server.
    e.g app.run(host="127.0.0.1", port=5001)
"""
app.run(debug=True)
