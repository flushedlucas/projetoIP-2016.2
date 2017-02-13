from tkinter import*
from tkinter import messagebox
from Arquivos import login, pessoas, estoque, vendas


class Pessoas:
    def montaCliente(self):
        nome = input("Digite o Nome: ")
        endereco = input("Digite o Endereço: ")
        bairro = input("Digite o Bairro: ")
        cidade = input("Digite o Cidade: ")
        cep = input("Digite o CEP: ")
        estado = input("Digite o Estado: ")
        telefone = input("Digite o Telefone: ")
        celular = input("Digite o Celular: ")
        fax = input("Digite o Fax: ")
        email = input("Digite o Email: ")
        rg = input("Digite o RG: ")
        cpf = input("Digite o CPF/CNPJ: ")
        data = input("Digite o Data de Nascimento: ")
        cliente = [nome, endereco, bairro, cidade, cep, estado, telefone, celular, fax, email, rg, cpf, data]
        return cliente

    def montaFornecedor(self):
        nome = input("Digite o Nome: ")
        cpf = input("Digite o CPF/CNPJ: ")
        contato = input("Digite o contato: ")
        endereco = input("Digite o Endereço: ")
        bairro = input("Digite o Bairro: ")
        cidade = input("Digite o Cidade: ")
        estado = input("Digite o Estado: ")
        cep = input("Digite o CEP: ")
        telefone = input("Digite o Telefone: ")
        celular = input("Digite o Celular: ")
        fax = input("Digite o Fax: ")
        fornecedor = [nome, cpf, contato, endereco, bairro, cidade, estado, cep, telefone, celular, fax]
        return fornecedor

    def montaFuncionario(self):
        nome = input("Digite o Nome: ")
        cargo = input("Digite o Cargo: ")
        data = input("Digite o Data de Nascimento: ")
        sexo = input("Digite o Sexo: ")
        endereco = input("Digite o Endereco: ")
        bairro = input("Digite o Bairro: ")
        cidade = input("Digite o Cidade: ")
        cep = input("Digite o CEP: ")
        estado = input("Digite o Estado: ")
        telefone = input("Digite o Telefone: ")
        celular = input("Digite o Celular: ")
        funcionario = [nome, cargo, data, sexo, endereco, bairro, cidade, cep, estado, telefone, celular]
        return funcionario

    def pesquisar(nome, opcao):
        nome = nome.lower()
        arq = open(opcao + ".txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[i] = j.split(",")
            for x in text:
                if x[0].lower() == nome:
                    return x
        return None

    def removerCliente(nome):
        remover = Pessoas.pesquisar(nome, "clientes")
        if remover != None:
            arq = open("clientes.txt")
            text = arq.readlines()
            arq.close()
            if text != None:
                for i, j in enumerate(text):
                    text[j] = i.split(" ")
                for x in text:
                    if x == remover:
                        text.remove(remover)
            arq = open("clientes.txt", "w")
            for t in text:
                for u in t:
                    arq.write(u + ",")
                arq.write("\n")
            arq.close()

    def removerFornecedor(nome):
        remover = Pessoas.pesquisar(nome, "fornecedores")
        if remover != None:
            arq = open("fornecedores.txt")
            text = arq.readlines()
            arq.close()
            if text != None:
                for i, j in enumerate(text):
                    text[j] = i.split(" ")
                for x in text:
                    if x == remover:
                        text.remove(remover)
            arq = open("fornecedores.txt", "w")
            for t in text:
                for u in t:
                    arq.write(u + ",")
                arq.write("\n")
            arq.close()

    def removerFuncionario(nome):
        remover = Pessoas.pesquisar(nome, "funcionarios")
        if remover != None:
            arq = open("funcionarios.txt")
            text = arq.readlines()
            arq.close()
            if text != None:
                for i, j in enumerate(text):
                    text[j] = i.split(" ")
                for x in text:
                    if x == remover:
                        text.remove(remover)
            arq = open("funcionarios.txt", "w")
            for t in text:
                for u in t:
                    arq.write(u + ",")
                arq.write("\n")
            arq.close()

    def consultar_cliente(nome):
        lista = Pessoas.pesquisar(nome, "clientes")
        if lista != None:
            print("""
            Nome: %s
            Endereço: %s
            Bairro: %s
            Cidade: %s
            CEP: %s
            Estado: %s
            Telefone: %s
            Celular: %s
            Fax: %s
            Email: %s
            RG: %s
            CPF/CNPJ: %s
            Data de Nascimento: %s\n""" % (
            lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
            lista[10], lista[11], lista[12]))
        else:
            print("Pessoa Nao Encontrada")

    def consultar_fornecedor(nome):
        lista = Pessoas.pesquisar(nome, "fornecedores")
        if lista != None:
            print("""Nome: %s
            CPF/CNPJ: %s
            Contato: %s
            Endereço: %s
            Bairro: %s
            Cidade: %s
            Estado: %s
            CEP: %s
            Telefone: %s
            Celular: %s
            Fax: %s""" % (
            lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
            lista[10]))
            return
        print("Pessoa Nao Encontrada")

    def consultar_funcionario(nome):
        lista = Pessoas.pesquisar(nome, "funcionarios")
        if lista != None:
            print("""Nome: %s
            Cargo: %s
            Data: %s
            Sexo: %s
            Endereço: %s
            Bairro: %s
            Cidade: %s
            CEP: %s
            Estado: %s
            Telefone: %s
            Celular: %s""" % (
            lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
            lista[10]))
            return
        print("Pessoa Nao Encontrada")

    def alterar_cliente(nome):
        alterar = Pessoas.pesquisar(nome, "clientes")
        if alterar != None:
            novo = Pessoas.montaCliente()
            arq = open("clientes.txt")
            text = arq.readlines()
            arq.close()
            if text != None:
                for i, j in enumerate(text):
                    text[j] = i.split(" ")
            for i, j in enumerate(text):
                if i == alterar:
                    text[j] = novo
            arq = open("clientes.txt", "w")
            for t in text:
                for u in t:
                    arq.write(u + ",")
                arq.write("\n")
            arq.close()

    def alterar_fornecedor(nome):
        alterar = Pessoas.pesquisar(nome, "fornecedores")
        if alterar != None:
            novo = Pessoas.montaFornecedor()
            arq = open("fornecedores.txt")
            text = arq.readlines()
            arq.close()
            if text != None:
                for i, j in enumerate(text):
                    text[j] = i.split(" ")
            for i, j in enumerate(text):
                if i == alterar:
                    text[j] = novo
            arq = open("fornecedores.txt", "w")
            for t in text:
                for u in t:
                    arq.write(u + ",")
                arq.write("\n")
            arq.close()

    def alterar_funcionario(nome):
        alterar = Pessoas.pesquisar(nome, "funcionarios")
        if alterar != None:
            novo = Pessoas.montaFuncionario()
            arq = open("funcionarios.txt")
            text = arq.readlines()
            arq.close()
            if text != None:
                for i, j in enumerate(text):
                    text[j] = i.split(" ")
            for i, j in enumerate(text):
                if i == alterar:
                    text[j] = novo
            arq = open("funcionarios.txt", "w")
            for t in text:
                for u in t:
                    arq.write(u + ",")
                arq.write("\n")
            arq.close()

    def adicionar_cliente(self):
        adiciona = Pessoas.montaCliente()
        arq = open("clientes.txt", "a")
        for i in adiciona:
            arq.write(i + ",")
        arq.write("\n")
        arq.close()

    def adicionar_fornecedor(self):
        adiciona = Pessoas.montaFornecedor()
        arq = open("fornecedores.txt", "a")
        for i in adiciona:
            arq.write(i + ",")
        arq.write("\n")
        arq.close()

    def adicionar_funcionario(self):
        adiciona = Pessoas.montaFuncionario()
        arq = open("funcionarios.txt", "a")
        for i in adiciona:
            arq.write(i + ",")
        arq.write("\n")
        arq.close()

    def iniciarPessoas(self):
        self.cadastro

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
        self.sistema["command"] = self.exibirSistema
        self.sistema.pack()

    def exibirSistema(self):
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
        #self.cadastro["command"] = pessoas.iniciar()
        self.cadastro.pack()

        self.estoque = Button(self.botaoEstoque)
        self.estoque["text"] = "Estoque"
        self.estoque["font"] = ("Calibri", "8")
        self.estoque["width"] = 12
        #self.estoque["command"] = estoque.iniciar()
        self.estoque.pack()

        self.relatorio = Button(self.botaoRelatorio)
        self.relatorio["text"] = "Relatório de Vendas"
        self.relatorio["font"] = ("Calibri", "8")
        self.relatorio["width"] = 20
        #self.relatorio["command"] = vendas.relatorio()
        self.relatorio.pack()

        self.sair = Button(self.botaoSair)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12
        self.sair["command"] = self.voltar
        self.sair.pack()

    def voltar(self):
        self.terceira.quit
        self.exibir()
        self.terceira.destroy()

root = Tk()
Application(root)
root.mainloop()