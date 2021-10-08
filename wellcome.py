import datetime
import pywhatkit


class entrada:

    def __init__(self, nome='', telefone='', demanda='', km='', receita='', ipk='', eqvl='', icv=''):

        nome = nome
        tel= "+55"+telefone
        self.demanda=''
        self.km=''
        self.receita=''
        self.ipk=''
        self.eqvl=''
        self.icv=''
        info = ''
        if demanda == 'Sim':
            info = info+" Demanda, "
        if km == 'Sim':
            info = info+" KM, "
        if receita == 'Sim':
            info = info+" Receita,  "
        if ipk == "Sim":
            info = info+" IPK, "
        if eqvl == "Sim":
            info = info+" Equivalência Tarifária,  "
        if icv == "Sim":
            info = info+" Índice de Cumprimento de Viagem,  "
        mensagem = f"Bem vindo(a) *{nome}*, a partir de hoje você receberá informações de: ({info}) da empresa HP Transportes"
        pywhatkit.sendwhatmsg_instantly(tel, mensagem, 15,  True)
