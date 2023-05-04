import sqlite3

conn = sqlite3.connect('colleges.db')

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS colleges (id int PRIMARY KEY, Region string NOT NULL, Name string NOT NULL, Category string, Url string)')
#c.execute('select distinct region insert from colleges '
