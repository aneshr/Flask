import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()

create = 'Create table if not exists users (id INTEGER PRIMARY KEY, username text, password text)' # use INTEGER for auto incrementing column

cur.execute(create)

create = 'Create table if not exists items (id INTEGER PRIMARY KEY, name text, price real)' # use INTEGER for auto incrementing column

cur.execute(create)

conn.commit()
conn.close()
