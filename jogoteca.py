# _*_ encoding: utf-8 _*_

from flask import Flask, render_template, request, redirect, session, flash, url_for


class Game:

    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

    def __str__(self):
        return f"Name -> {self.name} - " \
               f"Category -> {self.category} - " \
               f"Console -> {self.console}"


class User:

    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password


lewis = User('lewis', 'Lewis Hamilton', '444444')
charles = User('charles', 'Charles Leclerc', '333333', )
daniel = User('daniel', 'Daniel Ricciardo', '101010')

users = {lewis.user_id: lewis, charles.user_id: charles, daniel.user_id: daniel}

page_title = "Games"
game1 = Game('Super Mario', 'Action', 'SNT')
game2 = Game('Pokemon Gold', 'RPG', 'GBA')
games = [game1, game2]

app = Flask(__name__)
""" This is a sample web app. Never, never define secrete key in your source code... """
app.secret_key = "xvZkad019002863kajdh3hflskjgadçjeubdk"


@app.route('/')
def index():
    return render_template("games.html", title=page_title, games=games)


@app.route('/new')
def new_game():
    if 'logged_user' not in session or session['logged_user'] is None:
        return redirect(url_for('login', next_page=url_for('new_game')))

    return render_template('new_game.html', title=page_title)


@app.route('/create_game', methods=['POST', ])
def create_game():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    games.append(Game(name, category, console))

    return redirect(url_for('index'))


@app.route('/login')
def login():
    next_page = request.args.get('next_page')
    return render_template('login.html', next_page=next_page)


@app.route('/authenticate', methods=['POST', ])
def authenticate():

    if request.form['user'] in users:
        user = users[request.form['user']]
        if user.password == request.form['password']:
            session['logged_user'] = user.user_id
            flash(f'{user.name} logged successfully.')
            next_page = request.form['next_page']

            return redirect(next_page)

    flash('Not possible to perform login. Check your credentials.')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('No user logged.')
    return redirect(url_for('index'))


"""
    If necessary we can define host and port for our server.
    e.g app.run(host="127.0.0.1", port=5001)
"""
app.run(debug=True)
