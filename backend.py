import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY, word text, pronunciation text, definition text)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS rules (id INTEGER PRIMARY KEY, name text, rule text)')
        self.conn.commit()
