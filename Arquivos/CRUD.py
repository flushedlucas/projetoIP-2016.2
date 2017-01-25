def pesquisar(nome):
    nome = nome.lower()
    for i, j in enumerate(produto):
        if j[0].lower() == nome:
            return i
    return None

def remover():
    pass

def consultar():
    lista = pesquisar(nome)
    print("Nome: %s/n Endereço: %s/n Bairro: %s/n Cidade: %s/n CEP: %s/n Estado: %s/n Telefone: %s/n Celular: %s/n "
          "Fax: %s /n Email: %s/n RG: %s/n CPF/CNPJ: %s/n Data de Nascimento: %s/n "
          "Foto: %s/n")%(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8],
                         lista[9], lista[10], lista[11], lista[12], lista[13])

def alterar():
    pass

def adicionar():
    input("Digite o Nome: ")
    input("Digite o Endereço: ")
    input("Digite o Bairro: ")
    input("Digite o Cidade: ")
    input("Digite o CEP: ")
    input("Digite o Estado: ")
    input("Digite o Telefone: ")
    input("Digite o Celular: ")
    input("Digite o Fax: ")
    input("Digite o Email: ")
    input("Digite o RG: ")
    input("Digite o CPF/CNPJ: ")
    input("Digite o Data de Nascimento: ")
    input("Digite o Foto: ")