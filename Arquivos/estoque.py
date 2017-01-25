def montaProduto():
    codigo = input("Digite o código: ")
    categoria = input("Digite a Categoria: ")
    foto = input("Digite a Foto: ")
    descricao = input("Digite a descricao: ")
    estoqueMax = input("Digite o Estoque Maximo: ")
    estoqueMin = input("Digite o Estoque Minimo: ")
    valorvenda = input("Digite o Valor Base de Venda: ")
    valorcompra = input("Digite o Valor Base de Compra: ")
    produto = [codigo, categoria, foto, descricao, estoqueMax, estoqueMin, valorvenda, valorcompra]
    return produto

def abrir():
    arq = open("estoque.txt")
    text = arq.readlines()
    arq.close()
    if text != None:
        for i, j in enumerate(text):
            text[j] = i.split(" ")
        return arq
    return None

def pesquisar(nome):
    nome = nome.lower()
    produto = abrir()
    if produto != None:
        for i, j in enumerate(produto):
            if j[0].lower() == nome:
                return i
    return None

def remover(nome):
    remover = pesquisar(nome, "fornecedor")
    if remover != None:
        arq = open("fornecedor.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(" ")
            for x in text:
                if x == remover:
                    text.remove(remover)
        arq = open("fornecedor.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def consultar(nome):
    lista = pesquisar(nome, "fornecedor")
    if lista != None:
        print("""Codigo: %s
            Categoria: %s
            Foto: %s
            Descricao: %s
            Estoque Maximo: %s
            Estoque Minimo: %s
            Valor Base de Venda: %s
            Valor Base de Compra: %s""" % (
        lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10]))
        return
    print("Produto Nao Encontrado")

def alterar(nome):
    alterar = pesquisar(nome)
    if alterar != None:
        novo = montaProduto()
        arq = open("produto.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(" ")
        for i, j in enumerate(text):
            if i == alterar:
                text[j] = novo
        arq = open("produto.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def adicionar():
    adiciona = montaProduto()
    arq = open("produto.txt", "a")
    for i in adiciona:
        arq.write(i + ",")
    arq.write("\n")
    arq.close()

def iniciar():
    print("""
        Estoque

            1 - Cadastrar
            2 - Alterar
            3 - Consultar
            4 - Remover

        """)
    opcao = input("Opção: ")