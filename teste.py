from tkinter import *

root = Tk()

class aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.geometry('800x600')
        self.root.configure(background="#174155")
        
aplication()
