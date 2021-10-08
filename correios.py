from connect import bdados
from estagiario import Relatorio


class Entregador():

    def __init__(self):
        self.banco = bdados()
        self.cur = self.banco.con.cursor()
        self.cur.execute(
            "select * from usuarios")

        self.dadosUsuarios = {}
        i = 0

        for l in self.cur:
            self.dadosUsuarios[l[0]] = {'nome': l[1], 'tel': l[2], 'demanda': l[4], 'km': l[5], 'receita': l[6], 'ipk': l[7], 'eqvl': l[8]}
        self.cur.close()

    def KM(self):

        for i in range(len(self.dadosUsuarios)):
            if self.dadosUsuarios[1 + i]["km"] == 'Sim':
                Relatorio.quilometragem('+55' + self.dadosUsuarios[1 + i]["tel"], self.dadosUsuarios[1 + i]["nome"])
            if self.dadosUsuarios[1 + i]["ipk"] == 'Sim':
                Relatorio.ipk('+55' + self.dadosUsuarios[1 + i]["tel"], self.dadosUsuarios[1 + i]["nome"])

    def Demanda(self):

        for i in range(len(self.dadosUsuarios)):
            if self.dadosUsuarios[1 + i]["demanda"] == 'Sim':
                Relatorio.demanda('+55' + self.dadosUsuarios[1 + i]["tel"], self.dadosUsuarios[1 + i]["nome"])

            if self.dadosUsuarios[1 + i]["eqvl"] == 'Sim':
                Relatorio.eqvl('+55' + self.dadosUsuarios[1 + i]["tel"], self.dadosUsuarios[1 + i]["nome"])

            if self.dadosUsuarios[1 + i]["receita"] == 'Sim':
                Relatorio.receita('+55' + self.dadosUsuarios[1 + i]["tel"], self.dadosUsuarios[1 + i]["nome"])
