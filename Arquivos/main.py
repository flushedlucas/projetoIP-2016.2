from Arquivos import *
def exibir():
    print("""
        Sistemas de Vendas

        1 - Cadastro
        2 - Estoque
        3 - Relatorio de Vendas
        4 - Sair

        """)
    while True:
        escolha = input("Opção: ")
        if escolha == 1:
            print("""/n/nCadastro/n/n

                1 - Cadastrar
                2 - Alterar
                3 - Consultar
                4 - Remover

                 /n/n """)
            opcao = input("Opção: ")
            break
        elif escolha ==2:
            print("""/n/nEstoque/n/n

                1 - Cadastrar
                2 - Alterar
                3 - Consultar
                4 - Remover

            /n/n""")
            opcao = input("Opção: ")
            break
        elif escolha == 3:
            print("""/n/nVendas/n/n
                1 - Por Cliente
                2 - Por Vendedor
            """)
            break
        elif escolha == 4:
            break
        else:
            print("Opção inválida/n/n")

def login():
    while True:
        nome = input("Digite seu nome: ")
        login = input("Digite o Login: ")
        senha = input("Digite a Senha: ")
        result = login().buscar([nome, login, senha])
        if result == True:
            exibir()
            break
        else:
            print("Usuário ou Senha inválidos")