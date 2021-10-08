import sqlite3


class bdados:
    def __init__(self):
        self.con = sqlite3.connect('bdados.db')
        self.CreateTable()

    def CreateTable(self):
        cur = self.con.cursor()

        cur.execute("""create table  if not exists usuarios (
                    idUser integer primary key autoincrement ,
                    nome text,
                    telefone text,
                    email text,
                    demanda text,
                    km text,
                    receita text,
                    ipk text,
                    eqvl text
                    )""")
        self.con.commit()
        cur.close()
