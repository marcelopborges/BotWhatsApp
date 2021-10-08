from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")  # Definindo padrão de fonte
        self.containerPai = Frame(master)  # Definindo que o containerPai é o frame principal
        self.containerPai["pady"] = 10
        self.containerPai.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()

        self.title = Label(self.containerPai, text="Dados do usuário")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        # Nome
        self.nomeLabel = Label(self.container2, text="usuário:", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        # Campo de preenchimento Nome
        self.nome = Entry(self.container2)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        # Label Senha
        self.senhaLabel = Label(self.container3, text="Senha: ", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        # Campo de preenchimento de senha
        self.senha = Entry(self.container3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = '*'
        self.senha.pack(side=LEFT)

        self.conectar = Button(self.container4)
        self.conectar["text"] = "Conectar"
        self.conectar["font"] = ("Calibri", "8")
        self.conectar["width"] = 12
        self.conectar["command"] = self.VerificaSenha
        self.conectar.pack()

        self.msg = Label(self.container4, text="", font=self.fontePadrao)
        self.msg.pack()

    def VerificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "marcelo" and senha == "12345":
            self.msg["text"] = "Conectado!"
        else:
            self.msg["text"] = "Usuario ou senha incorreta!"


root = Tk()
Application(root)
root.mainloop()
