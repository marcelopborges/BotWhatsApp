from connect import bdados


class Users(object):

    def __init__(self, idUser="", nome="", telefone="", email="", demanda="", km="", receita="", ipk="", eqvl=""):
        self.info = {}
        self.idUser = idUser
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.demanda = demanda
        self.km = km
        self.receita = receita
        self.ipk = ipk
        self.eqvl = eqvl


    def InsertUser(self):

        banco = bdados()
        teste = (
                "insert into usuarios (nome, telefone, email, demanda, km, receita, ipk, eqvl) values ('" + self.nome + "', '" + self.telefone + "', '" +
                self.email + "', '" + self.demanda + "', '" + self.km + "', '" + self.receita + "', '" +
                self.ipk + "', '" + self.eqvl + "')"
        )
        try:
            cur = banco.con.cursor()
            cur.execute(
                "insert into usuarios (nome, telefone, email, demanda, km, receita, ipk, eqvl) values ('" + self.nome + "', '" + self.telefone + "', '" +
                self.email + "', '" + self.demanda + "', '" + self.km + "', '" + self.receita + "', '" +
                self.ipk + "', '" + self.eqvl + "')"
            )
            banco.con.commit()
            cur.close()

            return "Usuário cadastrado."
        except:
            return "Usuário não cadastrado, verifique os campos preenchidos."

    def UpdateUser(self):

        banco = bdados()

        try:

            cur = banco.con.cursor()
            cur.execute(
                "update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email +
                "', demanda = '" + self.demanda + "', km = '" + self.km + "', receita = '" + self.receita + "', ipk = '" + self.ipk +
                "', eqvl = '" + self.eqvl + "' where idUser = " + self.idUser + "")
            banco.con.commit()
            cur.close()

            return "Usuário atualizado"
        except:
            return "Usuário não atualizado, verifique os campos alterados"

    def DelUser(self):
        banco = bdados()

        try:
            cur = banco.con.cursor()
            cur.execute(
                "delete from usuarios where idUser = " + self.idUser + "")
            banco.con.commit()
            cur.close()

            return "Usuário deletado"
        except:
            return "Usuário não deletado, favor verificar os campos selecionados."

    def SelectUser(self, idUser):
        banco = bdados()

        try:

            cur = banco.con.cursor()
            cur.execute(
                "select * from usuarios where idUser = " + idUser + ""
            )

            for linha in cur:
                self.idUser = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                if linha[4] == 'Sim':
                    self.demanda = 1
                else:
                    self.demanda = 0

                if linha[5] == 'Sim':
                    self.km = 1
                else:
                    self.km = 0

                if linha[6] == 'Sim':
                    self.receita = 1
                else:
                    self.receita = 0

                if linha[7] == 'Sim':
                    self.ipk = 1
                else:
                    self.ipk = 0

                if linha[8] == 'Sim':
                    self.eqvl = 1
                else:
                    self.eqvl = 0



            cur.close()

            return "Busca feita com sucesso"
        except:
            return "Usuário não encontrado"


