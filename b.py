import sqlite3

class teste:
    def __init__(self):
        self.con = sqlite3.connect('bdados.db')
        self.cur = self.con.cursor()        
        self.cur.execute(
            "select * from usuarios")
        for l in self.cur:
            print (l)