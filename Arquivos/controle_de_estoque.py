def remover():
    pass

def consultar(nome):
    nome = nome.lower()
    for i, j in enumerate(produto):
        if j[0].lower() == nome:
            return i
    return None

def alterar():
    pass

def adicionar():
    pass
