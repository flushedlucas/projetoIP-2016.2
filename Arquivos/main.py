from tkinter import*
from tkinter import messagebox
from Arquivos import login, pessoas, estoque, vendas

class Application:
    def __init__(self, master = NONE):
        self.fontePadrao = ("Arial", "10")

        self.top = Frame(master)
        self.top.pack()

        self.principal = Frame(self.top)
        self.principal.pack()

        self.login()

    def login(self):

        self.primeiroContainer = Frame(self.principal)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.principal)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.principal)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.principal)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

    # Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        lista = [usuario.lower(), senha.lower()]
        result = login.buscar(lista)
        if result == True:
            self.principal.quit
            self.exibir()
            self.principal.destroy()
        else:
            self.nome.delete(0, END)
            self.senha.delete(0, END)
            messagebox.showerror("Erro", "Usuário ou Senha Inválidos")

    def exibir(self):
        lista = estoque.verificaEstoque()
        self.segunda = Frame(self.top)
        self.segunda.pack()
        if lista != None:
            lista = lista.join("\n")


            self.primeiroContainer = Frame(self.segunda)
            self.primeiroContainer["pady"] = 10
            self.primeiroContainer.pack()

            self.titulo = Label(self.primeiroContainer, text="lista")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()

        self.segundoContainer = Frame(self.segunda)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.segunda)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.segunda)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Comprar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = vendas.comprar()
        self.autenticar.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Vender"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = vendas.vender()
        self.autenticar.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Sistema"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.sistema
        self.autenticar.pack()

    def sistema(self):
        pass

root = Tk()
Application(root)
root.mainloop()