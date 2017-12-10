import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY, language text, english text, word text, pronunciation text, definition text)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS rules (id INTEGER PRIMARY KEY, language text, name text, rule text)')
        self.conn.commit()

    def insert_word(self,language,english,word,pronounciation,definition):
        self.cur.execute('INSERT INTO words VALUES (NULL,?,?,?,?,?)',(language,english,word,pronounciation,definition))
        self.conn.commit()

    def insert_rule(self,language,name,rule):
        self.cur.execute('INSERT INTO rules VALUES (NULL,?,?,?)',(language,name,rule))
        self.conn.commit()

    def view_all_words(self):
        self.cur.execute('SELECT * FROM words')
        rows=self.cur.fetchall()
        return rows

    def view_all_rules(self):
        self.cur.execute('SELECT * FROM rules')
        rows=self.cur.fetchall()
        return rows

    def search_words(self,language='',english='',word='',pronunciation='',definition=''):
        self.cur.execute('SELECT * FROM words WHERE language=? OR english=? OR word=? OR pronunciation=? OR definition=?', (language,english,word,pronunciation,definition))
        rows=self.cur.fetchall()
        return rows

    def search_rules(self,language='',name='',rule=''):
        self.cur.execute('SELECT * FROM rules WHERE language=? OR name=? OR rule=?', (language,name,rule))
        rows=self.cur.fetchall()
        return rows

    def delete_word(self,id):
        self.cur.execute('DELETE FROM words WHERE id=?',(id,))
        self.conn.commit()

    def delete_rule(self,id):
        self.cur.execute('DELETE FROM rules WHERE id=?',(id,))
        self.conn.commit()

    def update_word(self,id,language,english,word,pronunciation,definition):
        self.cur.execute('UPDATE words SET language=?, english=?, word=?, pronunciation=?, definition=? WHERE id=?',(language,english,word,pronunciation,definition,id))
        self.conn.commit()

    def update_rule(self,id,language,name,rule):
        self.cur.execute('UPDATE rules SET language=?, name=?, rule=? WHERE id=?',(language,name,rule,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#language_db = Database("mylanguage.db")
#language_db.insert_word("Tetzi","Hello","Teldi","TEHL-dee","A peaceful greeting; Love;")
#language_db.insert_rule("Tetzi","Random Rule","This is my rule.")
#language_db.delete_rule(2)
#language_db.update_word(1,"Tetzi","Hello","Teldi","TEHL-dee","A peaceful greeting; Love")
#language_db.update_rule(1, 'Tetzi', 'Possessive', 'Add “ahí” to the beginning of a word ending in “a”, “o”, or “u” to make it a possessive “my”, for words ending in “i”, add “ahó”')
#print(language_db.view_all_words())
#print(language_db.view_all_rules())
