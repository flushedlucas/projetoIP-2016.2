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

def remover():
    pass

def consultar(nome):
    pass

def alterar():
    pass

def adicionar():
    pass

def iniciar():
    print("""\n\n
                        Estoque

                            1 - Cadastrar
                            2 - Alterar
                            3 - Consultar
                            4 - Remover

                        """)
    opcao = input("Opção: ")