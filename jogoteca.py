# _*_ encoding: utf-8 _*_

from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL
from dao import JogoDao
from models import User, Game

lewis = User('lewis', 'Lewis Hamilton', '444444')
charles = User('charles', 'Charles Leclerc', '333333', )
daniel = User('daniel', 'Daniel Ricciardo', '101010')

users = {lewis.id: lewis, charles.id: charles, daniel.id: daniel}

page_title = "Games"

game1 = Game('Super Mario', 'Action', 'SNT')
game2 = Game('Pokemon Gold', 'RPG', 'GBA')
games = [game1, game2]

app = Flask(__name__)

""" This is a sample web app. Never, never define secrete key in your source code... """
app.secret_key = "xvZkad019002863kajdh3hflskjgadçjeubdk"

app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "sample"
app.config['MYSQL_PASSWORD'] = "123456"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app=app)
jogo_dao = JogoDao(db=db)


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

    # games.append(Game(name, category, console))
    jogo_dao.salvar(jogo=Game(name, category, console))

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
            session['logged_user'] = user.id
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
