def montaCliente():
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

def montaFornecedor():
    input("Digite o Nome: ")
    input("Digite o CPF/CNPJ: ")
    input("Digite o contato: ")
    input("Digite o Endereço: ")
    input("Digite o Bairro: ")
    input("Digite o Cidade: ")
    input("Digite o Estado: ")
    input("Digite o CEP: ")
    input("Digite o Telefone: ")
    input("Digite o Celular: ")
    input("Digite o Fax: ")

def montaFuncionario():
    input("Digite o Nome: ")
    input("Digite o Cargo: ")
    input("Digite o Data de Nascimento: ")
    input("Digite o Sexo: ")
    input("Digite o Endereco: ")
    input("Digite o Bairro: ")
    input("Digite o Cidade: ")
    input("Digite o CEP: ")
    input("Digite o Estado: ")
    input("Digite o Telefone: ")
    input("Digite o Celular: ")

def pesquisar(nome):
    nome = nome.lower()
    for i, j in enumerate(produto):
        if j[0].lower() == nome:
            return i
    return None

def remover():
    pass

def consultar(nome):
    lista = pesquisar(nome)
    if lista != None:
        print("Nome: %s\n Endereço: %s\n Bairro: %s\n Cidade: %s\n CEP: %s\n Estado: %s\n Telefone: %s\n Celular: %s\n "
              "Fax: %s \n Email: %s\n RG: %s\n CPF/CNPJ: %s\n Data de Nascimento: %s\n "
              "Foto: %s\n")%(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8],
                             lista[9], lista[10], lista[11], lista[12], lista[13])
        return
    print("Pessoa Nao Encontrada")

def alterar_cliente():
    montaCliente()

def alterar_fornecedor():
    montaFornecedor()

def alterar_funcionario():
    montaFuncionario()

def adicionar_cliente():
    montaCliente()

def adicionar_fornecedor():
    montaFornecedor()

def adicionar_funcionario():
    montaFuncionario()

def iniciar():
    while True:
        print("""\n\n
                Cadastro

                    1 - Adicionar
                    2 - Alterar
                    3 - Consultar
                    4 - Remover
                    5 - Voltar

                     """)
        opcao = input("Opção: ")
        if opcao == str(1):
            pass
        elif opcao == str(2):
            pass
        elif opcao == str(3):
            pass
        elif opcao == str(4):
            pass
        elif opcao == str(5):
            break
        else:
            print("\nOpcao Invalida\n")