from tkinter import*
from tkinter import messagebox
from Arquivos import login, pessoas, estoque, vendas

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
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
            exibir()
        else:
            self.nome["text"] = ""
            self.senha["text"] = ""
            messagebox.showerror("Erro", "Usuário ou Senha Inválidos")

    def exibir(self):
        pass

def exibir():
    estoque.verificaEstoque()
    while True:
        print("""
            1 - Comprar
            2 - Vender
            3 - Sistema
        """)
        selecao = input("Opcao: ")
        if selecao == str(1):
            vendas.comprar()
            break
        elif selecao == str(2):
            vendas.vender()
            break
        elif selecao == str(3):
            print("""
                Sistemas de Vendas

                1 - Cadastro
                2 - Estoque
                3 - Relatorio de Vendas
                4 - Sair

                """)
            escolha = input("Opção: ")
            if escolha == str(1):
                pessoas.iniciar()
            elif escolha == str(2):
                estoque.iniciar()
            elif escolha == str(3):
                vendas.relatorio()
            elif escolha == str(4):
                break
            else:
                print("Opção inválida\n\n")

root = Tk()
Application(root)
root.mainloop()