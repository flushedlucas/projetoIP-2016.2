def montaProduto():
    codigo = input("Digite o código: ")
    categoria = input("Digite a Categoria: ")
    descricao = input("Digite a descricao: ")
    estoqueMax = input("Digite o Estoque Maximo: ")
    estoqueMin = input("Digite o Estoque Minimo: ")
    valorvenda = input("Digite o Valor Base de Venda: ")
    valorcompra = input("Digite o Valor Base de Compra: ")
    produto = [codigo, categoria, descricao, estoqueMax, estoqueMin, valorvenda, valorcompra]
    return produto

def abrir():
    arq = open("produtos.txt")
    text = arq.readlines()
    arq.close()
    if text != None:
        for i, j in enumerate(text):
            text[i] = j.split(",")
        return arq
    return None

def pesquisar(codigo):
    codigo = codigo.lower()
    arq = open("produtos.txt")
    produto = arq.readlines()
    arq.close()
    if produto != None:
        for i, j in enumerate(produto):
            produto[i] = j.split(",")
        for i, j in enumerate(produto):
            if j[0].lower() == codigo:
                return j
    return None

def remover(codigo):
    remover = pesquisar(codigo)
    if remover != None:
        arq = open("produtos.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(",")
            for x in text:
                if x == remover:
                    text.remove(remover)
        arq = open("produtos.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def consultar(codigo):
    lista = pesquisar(codigo)
    if lista != None:
        print("""Codigo: %s
            Categoria: %s
            Descricao: %s
            Estoque Maximo: %s
            Estoque Minimo: %s
            Valor Base de Venda: %s
            Valor Base de Compra: %s""" % (
        lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6]))
        return
    print("Produto Nao Encontrado")


def vender():
    codigo = input("Digite o codigo do produto: ")
    if codigo != None:
        produto = pesquisar(codigo)
        if produto != None:
            qtd = input("Digite a quantidade: ")
            if qtd != None:
                arq = open("estoque.txt")
                text = arq.readlines()
                arq.close()
                if text != None:
                    for i, j in enumerate(text):
                        text[i] = j.split(",")
                for i, j in enumerate(text):
                    if j[0] == produto[0]:
                        if int(text[i][1]) - int(qtd) >= 0:
                            text[i][1] = str(int(text[i][1]) - int(qtd))
                        else:
                            print("Nao existem produtos em estoque suficiente")
                arq = open("estoque.txt", "w")
                for t in text:
                    for u in t:
                        if u != '' and u != "\n":
                            arq.write(u + ",")
                    arq.write("\n")
                arq.close()

def comprar():
    codigo = input("Digite o codigo do produto: ")
    if codigo != None:
        produto = pesquisar(codigo)
        if produto != None:
            qtd = input("Digite a quantidade: ")
            if qtd != None:
                listavazia = []
                achou = False
                arq = open("estoque.txt")
                text = arq.readlines()
                arq.close()
                if text != None and text != listavazia:
                    for i, j in enumerate(text):
                        text[i] = j.split(",")
                    for i, j in enumerate(text):
                        if j[0] == produto[0]:
                            if int(text[i][1]) + int(qtd) <= int(text[i][2]):
                                text[i][1] = str(int(text[i][1]) + int(qtd))
                                achou = True
                            else:
                                print("Quantidade de produtos em estoque acima do permitido")
                    arq = open("estoque.txt", "w")
                    for t in text:
                        for u in t:
                            if u != '' and u != "\n":
                                arq.write(u + ",")
                        arq.write("\n")
                    arq.close()
                if achou == False:
                    arq = open("estoque.txt", "a")
                    arq.write(produto[0] +"," + qtd + "," + produto[3] + ","+ produto[4] + "," + "\n")
                    arq.close()
        else:
            print("Produto nao encontrado.")


def alterar(codigo):
    alterar = pesquisar(codigo)
    if alterar != None:
        novo = montaProduto()
        arq = open("produtos.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[i] = j.split(",")
        for i, j in enumerate(text):
            if j == alterar:
                text[i] = novo
        arq = open("produtos.txt", "w")
        for t in text:
            for u in t:
                if u != '' and u != "\n":
                    arq.write(u + ",")
            arq.write("\n")
        arq.close()
    else:
        print("Produto nao encontrado")

def adicionar():
    adiciona = montaProduto()
    arq = open("produtos.txt", "a")
    for i in adiciona:
        arq.write(i + ",")
    arq.write("\n")
    arq.close()

def verificaEstoque():
    arq = open("estoque.txt")
    text = arq.readlines()
    arq.close()
    if text != None:
        for i, j in enumerate(text):
            text[i] = j.split(",")
            if int(text[i][1]) < int(text[i][3]):
                print("Produto " + text[i][0] + " com estoque baixo.")

def iniciar():
    while True:
        print("""
            Estoque

                1 - Cadastrar
                2 - Alterar
                3 - Consultar
                4 - Remover

            """)
        opcao = input("Opção: ")
        if opcao == str(1):
            adicionar()
            break
        elif opcao == str(2):
            escolha = input("Digite o codigo do produto: ")
            if escolha != None:
                alterar(escolha)
            break
        elif opcao == str(3):
            escolha = input("Digite o codigo do produto: ")
            consultar(escolha)
            break
        elif opcao == str(4):
            escolha = input("Digite o codigo do produto: ")
            remover(escolha)
            break
        elif opcao == str(5):
            break
        else:
            print("Opcao Invalida")

