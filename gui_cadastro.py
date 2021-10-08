from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk

import wellcome
from users import *
from validation import validate


class App():

    def __init__(self, master=None):
        self.fontePadrao = ("Verdana", "8")

        # criação dos containers
        self.container1 = Frame(master)
        self.container1["padx"] = 100
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 100
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 100
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 100
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 100
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 100
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 100
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 100
        self.container8["pady"] = 5
        self.container8.pack()

        # Frames dos combobox
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()

        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()

        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()

        self.container12 = Frame(master)
        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.pack()

        self.container13 = Frame(master)
        self.container13["padx"] = 20
        self.container13["pady"] = 5
        self.container13.pack()

        self.container14 = Frame(master)
        self.container14["padx"] = 20
        self.container14["pady"] = 5
        self.container14.pack()

        self.container15 = Frame(master)
        self.container15["padx"] = 20
        self.container15["pady"] = 5
        self.container15.pack()

        # titulo
        self.title = Label(self.container1, text="Informe os dados: ")
        self.title["font"] = ("Calibri", "12", "bold")
        self.title.pack()

        self.lblIdUser = Label(self.container2, text="ID do usuário:", font=self.fontePadrao, width=12)
        self.lblIdUser.pack(side=LEFT)

        self.txtIdUser = Entry(self.container2)
        self.txtIdUser["width"] = 10
        self.txtIdUser["font"] = self.fontePadrao
        self.txtIdUser.pack(side=LEFT)

        self.btnIdUserSearch = Button(self.container2, text="Buscar", font=self.fontePadrao, width=10)
        self.btnIdUserSearch["command"] = self.SearchUser
        self.btnIdUserSearch.pack(side=RIGHT)

        self.lblName = Label(self.container3, text="Nome:", font=self.fontePadrao, width=10)
        self.lblName.pack(side=LEFT)

        self.txtName = Entry(self.container3)
        self.txtName["width"] = 50
        self.txtName["font"] = self.fontePadrao
        self.txtName.pack(side=LEFT)

        self.lblTel = Label(self.container4, text="Telefone:", font=self.fontePadrao, width=10)
        self.lblTel.pack(side=LEFT)

        self.txtTel = Entry(self.container4)
        self.txtTel["width"] = 50
        self.txtTel["font"] = self.fontePadrao
        self.txtTel.pack(side=LEFT)

        self.lblEmail = Label(self.container5, text="Email: ", font=self.fontePadrao, width=10)
        self.lblEmail.pack(side=LEFT)

        self.txtEmail = Entry(self.container5)
        self.txtEmail["width"] = 50
        self.txtEmail["font"] = self.fontePadrao
        self.txtEmail.pack(side=LEFT)



        # Labels e combobox

        # titulo
        self.title = Label(self.container6, text="Selecione os dados permitidos para envio")
        self.title["font"] = ("Calibri", "12", "bold")
        self.title.pack()

        self.lblDemanda = Label(self.container7, text="Demanda:", justify=LEFT)
        self.lblDemanda["font"] = self.fontePadrao
        self.lblDemanda["width"] = 30
        self.lblDemanda.pack(side=LEFT)

        self.comboDemanda = ttk.Combobox(self.container7, values=["Não", "Sim"], state="readonly")
        self.comboDemanda["font"] = self.fontePadrao
        self.comboDemanda.pack(side=RIGHT)
        self.comboDemanda.current(0)

        self.lblKm = Label(self.container8, text="Quilometragem:", justify=LEFT)
        self.lblKm["font"] = self.fontePadrao
        self.lblKm["width"] = 30
        self.lblKm.pack(side=LEFT)

        self.comboKM = ttk.Combobox(self.container8, values=["Não", "Sim"], state="readonly")
        self.comboKM["font"] = self.fontePadrao
        self.comboKM.pack(side=RIGHT)
        self.comboKM.current(0)

        self.lblReceita = Label(self.container9, text="Receita:", justify=LEFT)
        self.lblReceita["font"] = self.fontePadrao
        self.lblReceita["width"] = 30
        self.lblReceita.pack(side=LEFT)

        self.comboReceita = ttk.Combobox(self.container9, values=["Não", "Sim"], state="readonly")
        self.comboReceita["font"] = self.fontePadrao
        self.comboReceita.pack(side=RIGHT)
        self.comboReceita.current(0)

        self.lblIPK = Label(self.container10, text="IPK:", justify=LEFT)
        self.lblIPK["font"] = self.fontePadrao
        self.lblIPK["width"] = 30
        self.lblIPK.pack(side=LEFT)

        self.comboIPK = ttk.Combobox(self.container10, values=["Não", "Sim"], state="readonly")
        self.comboIPK["font"] = self.fontePadrao
        self.comboIPK.pack(side=RIGHT)
        self.comboIPK.current(0)

        self.lblEQVL = Label(self.container11, text="Equivalência Tarifária:", justify=LEFT)
        self.lblEQVL["font"] = self.fontePadrao
        self.lblEQVL["width"] = 30
        self.lblEQVL.pack(side=LEFT)

        self.comboEQVL = ttk.Combobox(self.container11, values=["Não", "Sim"], state="readonly")
        self.comboEQVL["font"] = self.fontePadrao
        self.comboEQVL.pack(side=RIGHT)
        self.comboEQVL.current(0)

        '''self.lblICV = Label(self.container12, text="Índice de Cumprimento de viagem:", justify=LEFT)
        self.lblICV["font"] = self.fontePadrao
        self.lblICV["width"] = 30
        self.lblICV.pack(side=LEFT)

        self.comboICV = ttk.Combobox(self.container12, values=["Não", "Sim"], state="readonly")
        self.comboICV["font"] = self.fontePadrao
        self.comboICV.pack(side=RIGHT)
        self.comboICV.current(0)'''

        # Botões CRUD

        self.btnInsert = Button(self.container13, text="Inserir", font=self.fontePadrao, width=12)
        self.btnInsert["command"] = self.InsertUser
        self.btnInsert.pack(side=LEFT)

        self.btnUpdate = Button(self.container13, text="Atualizar", font=self.fontePadrao, width=12)
        self.btnUpdate["command"] = self.AlterUser
        self.btnUpdate.pack(side=LEFT)

        self.btnDel = Button(self.container13, text="Deletar", font=self.fontePadrao, width=12)
        self.btnDel["command"] = self.DeleteUser
        self.btnDel.pack(side=LEFT)

        # Botão mostrar Treeview

        self.btnView = Button(self.container14, text="Listar Usuários", font=self.fontePadrao, width=12)
        self.btnView["command"] = self.listView
        self.btnView.pack(side=LEFT)



        # Mensagem de ação

        self.lblMsg = Label(self.container15, text="")
        self.lblMsg["font"] = ("Verdana", "9", "italic")
        self.lblMsg.pack()

    def InsertUser(self):
        user = Users()
        user.nome = self.txtName.get()
        user.telefone = self.txtTel.get()
        if validate.tel(user.telefone):
            pass
        else:
            msg.showerror("Erro de preenchimento", "Favor insira o número igual está no whatsApp (Não precisa colocar o +55 e nem os "-"")
            root.mainloop()

        user.email = self.txtEmail.get()
        if validate.mail(user.email):
            pass
        else:
            msg.showerror("Erro de preenchimento", "O email está inválido, favor verificar.")
            root.mainloop()

        user.demanda = self.comboDemanda.get()
        user.km = self.comboKM.get()
        user.receita = self.comboReceita.get()
        user.ipk = self.comboIPK.get()
        user.eqvl = self.comboEQVL.get()


        self.lblMsg["text"] = user.InsertUser()
        wellcome.entrada(user.nome, user.telefone, user.demanda, user.km, user.receita, user.ipk, user.eqvl)

        self.txtIdUser.delete(0, END)
        self.txtName.delete(0, END)
        self.txtTel.delete(0, END)
        self.txtEmail.delete(0, END)
        self.comboDemanda.current(0)
        self.comboKM.current(0)
        self.comboReceita.current(0)
        self.comboIPK.current(0)
        self.comboEQVL.current(0)



    def AlterUser(self):
        user = Users()

        user.idUser = self.txtIdUser.get()
        user.nome = self.txtName.get()
        user.telefone = self.txtTel.get()
        user.email = self.txtEmail.get()
        user.demanda = self.comboDemanda.get()
        user.km = self.comboKM.get()
        user.receita = self.comboReceita.get()
        user.ipk = self.comboIPK.get()
        user.eqvl = self.comboEQVL.get()


        self.lblMsg["text"] = user.UpdateUser()
        wellcome.entrada(user.nome, user.telefone, user.demanda, user.km, user.receita, user.ipk, user.eqvl)

        self.txtIdUser.delete(0, END)
        self.txtName.delete(0, END)
        self.txtTel.delete(0, END)
        self.txtEmail.delete(0, END)
        self.comboDemanda.current(0)
        self.comboKM.current(0)
        self.comboReceita.current(0)
        self.comboIPK.current(0)
        self.comboEQVL.current(0)


    def DeleteUser(self):
        user = Users()

        user.idUser = self.txtIdUser.get()
        user.nome = self.txtName.get()
        user.telefone = self.txtTel.get()
        user.email = self.txtEmail.get()
        user.demanda = self.comboDemanda.get()
        user.km = self.comboKM.get()
        user.receita = self.comboReceita.get()
        user.ipk = self.comboIPK.get()
        user.eqvl = self.comboEQVL.get()


        self.lblMsg["text"] = user.DelUser()

        self.txtIdUser.delete(0, END)
        self.txtName.delete(0, END)
        self.txtTel.delete(0, END)
        self.txtEmail.delete(0, END)
        self.comboDemanda.current(0)
        self.comboKM.current(0)
        self.comboReceita.current(0)
        self.comboIPK.current(0)
        self.comboEQVL.current(0)


    def SearchUser(self):
        user = Users()

        idUser = self.txtIdUser.get()
        self.lblMsg["text"] = user.SelectUser(idUser)

        self.txtName.delete(0, END)
        self.txtName.insert(INSERT, user.nome)

        self.txtTel.delete(0, END)
        self.txtTel.insert(INSERT, user.telefone)

        self.txtEmail.delete(0, END)
        self.txtEmail.insert(INSERT, user.email)

        self.comboDemanda.current(0)
        self.comboDemanda.current(user.demanda)

        self.comboKM.current(0)
        self.comboKM.current(user.km)

        self.comboReceita.current(0)
        self.comboReceita.current(user.receita)

        self.comboIPK.current(0)
        self.comboIPK.current(user.ipk)

        self.comboEQVL.current(0)
        self.comboEQVL.current(user.eqvl)



    def listView(self):
        bdados()
        root2 = Tk()
        root2.geometry("1200x600")

        self.tree = ttk.Treeview(root2, column=(
        "idUser", "nome", "telefone", "email", "demanda", "km", "receita", "ipk", "eqvl"), show='headings')
        # formatação das colunas do treeview
        self.tree.column("#1", width=20, anchor="center")
        self.tree.column("#2", width=100, anchor="center")
        self.tree.column("#3", width=100, anchor="center")
        self.tree.column("#4", width=300, anchor="center")
        self.tree.column("#5", width=100, anchor="center")
        self.tree.column("#6", width=100, anchor="center")
        self.tree.column("#7", width=75, anchor="center")
        self.tree.column("#8", width=75, anchor="center")
        self.tree.column("#9", width=75, anchor="center")


        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="NOME")
        self.tree.heading("#3", text="TELEFONE")
        self.tree.heading("#4", text="EMAIL")
        self.tree.heading("#5", text="DEMANDA")
        self.tree.heading("#6", text="QUILOMETRAGEM")
        self.tree.heading("#7", text="RECEITA")
        self.tree.heading("#8", text="IPK")
        self.tree.heading("#9", text="EQVL")

        self.tree.pack()
        self.View()

        btn = Button(root2, text="Fechar", command=root2.destroy)
        btn.pack()
        root2.mainloop()

    def View(self):
        banco = bdados()
        try:
            cur = banco.con.cursor()
            cur.execute("SELECT * FROM usuarios")
            rows = cur.fetchall()

            for row in rows:
                self.tree.insert("", END, values=row)
            banco.con.close()
        except:
            print("erro")


root = Tk()
root.iconbitmap('./images/logo.ico')
root.title("Cadastro de usuários e permissões de acesso - MsnHP")
App(root)
root.mainloop()
