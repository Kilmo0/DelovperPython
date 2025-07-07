from tkinter import *

root = Tk()

class aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.botões()
        self.root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.geometry('600x400')
        self.root.configure(background="#174155")
        self.root.resizable(False, False)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    
    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg="#C0C0C0",
                            highlightbackground="#000000", highlightthickness=2)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame2 = Frame(self.root, bd=4, bg="#D4D4D4",
                           highlightbackground='#000000', highlightthickness=2)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def botões(self):
        self.limpar = Button(self.frame1, text='Limpar', bd=2, bg="#EAFEFF", fg="#2C2929",
                              font=('Arial', 8, 'bold'))
        self.limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        self.buscar = Button(self.frame1, text='Buscar')
        self.buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        self.procurar = Button(self.frame1, text='Procurar')
        self.procurar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        self.alterar = Button(self.frame1, text='Alterar')
        self.alterar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        self.novo = Button(self.frame1, text='Novo')
        self.novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        #Labels
        self.lbcodigo = Label(self.frame1, text="Código")
        self.lbcodigo.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.1)
        self.lbnome = Label(self.frame1, text='Nome')
        self.lbnome.place(relx=0.05, rely=0.4, relwidth=0.1, relheight=0.1)
        self.lbtelefone = Label(self.frame1, text='Telefone')
        self.lbtelefone.place(relx=0.05, rely=0.7, relwidth=0.1, relheight=0.1)
        self.lbcidade = Label(self.frame1, text='Cidade')
        self.lbcidade.place(relx=0.5, rely=0.7, relheight=0.1, relwidth=0.1)

        #inputspace
        self.codeinput = Entry(self.frame1)
        self.codeinput.place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.1)
        self.nomeinput = Entry(self.frame1)
        self.nomeinput.place(relx=0.05, rely=0.5, relwidth=0.8, relheight=0.1)
        self.teleinput = Entry(self.frame1)
        self.teleinput.place(relx=0.05, rely=0.8, relwidth=0.4, relheight=0.1)
        self.cidadeinput = Entry(self.frame1)
        self.cidadeinput.place(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.1)



aplication()
 