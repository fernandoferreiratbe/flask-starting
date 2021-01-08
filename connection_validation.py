# _*_ encoding: utf-8 _*_


import MySQLdb

connection = MySQLdb.connect(user='Username',
                             passwd='password',
                             db='databasename',
                             host='host',
                             port=3306)

# connection.open()

# cursor = connection.cursor()
cursor = connection.cursor()
# cursor.execute("INSERT INTO usuario (id, nome, senha) "
#                "VALUES (%s, %s, %s)"
#                , ('luan', 'Luan Marques', 'flask'))

cursor.execute("TRUNCATE usuario")

cursor.executemany("INSERT INTO usuario (id, nome, senha) VALUES (%s, %s, %s)",
                   [
                       ('luan', 'Luan Marques', '****'),
                       ('nico', 'Nico Steppat', '****'),
                       ('Danilo', 'Danilo Oliveira', '*****')
                   ])

cursor.execute("SELECT * FROM usuario")

for usuario in cursor.fetchall():
    print(usuario[0])

connection.commit()
connection.close()
