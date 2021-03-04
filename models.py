# _*_ encoding: utf-8 _*_


class Game:

    def __init__(self, name, category, console, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.console = console

    def __str__(self):
        return f"Name -> {self.name} - " \
               f"Category -> {self.category} - " \
               f"Console -> {self.console}"


class User:

    def __init__(self, user_id, name, password):
        self.id = user_id
        self.name = name
        self.password = password
