from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class funcoes():
    def limpartela(self):
        self.codeinput.delete(0, END)
        self.nomeinput.delete(0, END)
        self.teleinput.delete(0, END)
        self.cidadeinput.delete(0, END)
    def sqlconect(self):
        self.conn = sqlite3.connect('Clientes.db'); print('Conectando ao banco de dados')
        self.cursor = self.conn.cursor()
    def sqldesconect(self):
        self.conn.close(); print('Desconectando Banco de Dados')
    def tabela(self):
        self.sqlconect(); print("Conectando Banco de Dados")
        ###Tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nomecliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade INTEGER(40)
            );
            """)
        self.conn.commit(); print('Banco de dados Criado')
        self.sqldesconect() 

class application(funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.botões()
        self.lista()
        self.tabela()
        self.root.mainloop()
    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.geometry('600x400')
        self.root.configure(background="#174155")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)
    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg="#E7F3FF",
                            highlightbackground="#091B2A", highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame2 = Frame(self.root, bd=4, bg="#E7F3FF",
                           highlightbackground='#091B2A', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def botões(self):
        self.limpar = Button(self.frame1, text='Limpar', bd=2, bg="#1A2C56", fg="#FFFFFF",
                              font=('Aptos', 8, 'bold'), command=self.limpartela)
        self.limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        self.buscar = Button(self.frame1, text='Buscar', bd=2, bg="#1A2C56", fg="#FFFFFF",
                             font=('Aptos', 8, 'bold'))
        self.buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        self.procurar = Button(self.frame1, text='Procurar', bd=2, bg='#1A2C56', fg='#FFFFFF',
                               font=('Aptos', 8, 'bold'))
        self.procurar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        self.alterar = Button(self.frame1, text='Alterar', bd=2, bg='#1A2C56', fg='#FFFFFF',
                              font=('Aptos', 8, 'bold'))
        self.alterar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        self.novo = Button(self.frame1, text='Novo', bg='#1A2C56', fg='#ffffff',
                           font=('Aptos', 8, 'bold'))
        self.novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        #Labels
        self.lbcodigo = Label(self.frame1, text="Código", bg='#E7F3FF', fg='#1A2C56', font=('Aptos', 8, 'bold'))
        self.lbcodigo.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.1)
        self.lbnome = Label(self.frame1, text='Nome', bg='#E7F3FF', fg='#1A2C56', font=('Aptos', 8, 'bold'))
        self.lbnome.place(relx=0.03, rely=0.4, relwidth=0.1, relheight=0.1)
        self.lbtelefone = Label(self.frame1, text='Telefone', bg='#E7F3FF', fg='#1A2C56', font=('Aptos', 8, 'bold'))
        self.lbtelefone.place(relx=0.04, rely=0.7, relwidth=0.1, relheight=0.1)
        self.lbcidade = Label(self.frame1, text='Cidade', bg='#E7F3FF', fg='#1A2C56', font=('Aptos', 8, 'bold'))
        self.lbcidade.place(relx=0.5, rely=0.7, relheight=0.1, relwidth=0.1)

        #inputspace
        self.codeinput = Entry(self.frame1,)
        self.codeinput.place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.1)
        self.nomeinput = Entry(self.frame1)
        self.nomeinput.place(relx=0.05, rely=0.5, relwidth=0.8, relheight=0.1)
        self.teleinput = Entry(self.frame1)
        self.teleinput.place(relx=0.05, rely=0.8, relwidth=0.4, relheight=0.1)
        self.cidadeinput = Entry(self.frame1)
        self.cidadeinput.place(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.1)
    def lista(self):
        self.list = ttk.Treeview(self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.list.heading("#0", text="")
        self.list.heading("#1", text="Código")
        self.list.heading("#2", text="Nome")
        self.list.heading("#3", text="Telefone")
        self.list.heading("#4", text="Cidade")

        self.list.column('#0', width=1)
        self.list.column('#1', width=50) 
        self.list.column('#2', width=200) 
        self.list.column('#3', width=125) 
        self.list.column('#4', width=125) 

        self.list.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)
        self.scroll = Scrollbar(self.frame2, orient='vertical')
        self.list.configure(yscroll = self.scroll.set)
        self.scroll.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.85)

application()