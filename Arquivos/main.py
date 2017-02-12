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

        self.textoUsuario = Frame(self.principal)
        self.textoUsuario["pady"] = 10
        self.textoUsuario.pack()

        self.nomeContainer = Frame(self.principal)
        self.nomeContainer["padx"] = 20
        self.nomeContainer.pack()

        self.senhaContainer = Frame(self.principal)
        self.senhaContainer["padx"] = 20
        self.senhaContainer.pack()

        self.botaoEntrar = Frame(self.principal)
        self.botaoEntrar["pady"] = 20
        self.botaoEntrar.pack()

        self.titulo = Label(self.textoUsuario, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.nomeContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.nomeContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.senhaContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.senhaContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.botaoEntrar)
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

            self.avisoEstoque = Frame(self.segunda)
            self.avisoEstoque["pady"] = 10
            self.avisoEstoque.pack(side = TOP)

            self.titulo = Label(self.avisoEstoque, text="lista")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()

        self.botaoComprar = Frame(self.segunda)
        self.botaoComprar["padx"] = 20
        self.botaoComprar.pack()

        self.botaoVender = Frame(self.segunda)
        self.botaoVender["padx"] = 20
        self.botaoVender.pack()

        self.botaoSistema = Frame(self.segunda)
        self.botaoSistema["pady"] = 20
        self.botaoSistema.pack()

        self.comprar = Button(self.botaoComprar)
        self.comprar["text"] = "Comprar"
        self.comprar["font"] = ("Calibri", "8")
        self.comprar["width"] = 12
        #self.comprar["command"] = vendas.comprar()
        self.comprar.pack()

        self.vender = Button(self.botaoVender)
        self.vender["text"] = "Vender"
        self.vender["font"] = ("Calibri", "8")
        self.vender["width"] = 12
        #self.vender["command"] = vendas.vender()
        self.vender.pack()

        self.sistema = Button(self.botaoSistema)
        self.sistema["text"] = "Sistema"
        self.sistema["font"] = ("Calibri", "8")
        self.sistema["width"] = 12
        #self.sistema["command"] = self.sistema()
        self.sistema.pack()

    def sistema(self):
        self.segunda.quit
        self.segunda.destroy()
        self.terceira = Frame(self.top)
        self.terceira.pack()

        self.botaoCadastro = Frame(self.terceira)
        self.botaoCadastro["pady"] = 10
        self.botaoCadastro.pack()

        self.botaoEstoque = Frame(self.terceira)
        self.botaoEstoque["padx"] = 20
        self.botaoEstoque.pack()

        self.botaoRelatorio = Frame(self.terceira)
        self.botaoRelatorio["padx"] = 20
        self.botaoRelatorio.pack()

        self.botaoSair = Frame(self.terceira)
        self.botaoSair["pady"] = 20
        self.botaoSair.pack()

        self.cadastro = Button(self.botaoCadastro)
        self.cadastro["text"] = "Cadastro"
        self.cadastro["font"] = ("Calibri", "8")
        self.cadastro["width"] = 12
        self.cadastro["command"] = pessoas.iniciar()
        self.cadastro.pack()

        self.estoque = Button(self.botaoEstoque)
        self.estoque["text"] = "Estoque"
        self.estoque["font"] = ("Calibri", "8")
        self.estoque["width"] = 12
        self.estoque["command"] = estoque.iniciar()
        self.estoque.pack()

        self.relatorio = Button(self.botaoRelatorio)
        self.relatorio["text"] = "Relatório de Vendas"
        self.relatorio["font"] = ("Calibri", "8")
        self.relatorio["width"] = 12
        self.relatorio["command"] = vendas.relatorio()
        self.relatorio.pack()

        self.sair = Button(self.botaoSair)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12
        self.sair["command"] = self.exibir()
        self.sair.pack()

root = Tk()
Application(root)
root.mainloop()