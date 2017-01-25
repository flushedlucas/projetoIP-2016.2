from Arquivos import login
def exibir():

    while True:
        print("""
            1 - Comprar
            2 - Vender
            3 - Sistema
        """)
        selecao = input("Opcao: ")
        if selecao == str(1):
            pass
        elif selecao == str(2):
            pass
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
                    print("""\n\n
                    Cadastro

                        1 - Cadastrar
                        2 - Alterar
                        3 - Consultar
                        4 - Remover

                         """)
                    opcao = input("Opção: ")
                    break
                elif escolha == str(2):
                    print("""\n\n
                    Estoque

                        1 - Cadastrar
                        2 - Alterar
                        3 - Consultar
                        4 - Remover

                    """)
                    opcao = input("Opção: ")
                    break
                elif escolha == str(3):
                    print("""\n\n
                    Vendas

                        1 - Por Cliente
                        2 - Por Vendedor

                    """)
                    break
                elif escolha == str(4):
                    break
                else:
                    print("Opção inválida\n\n")

def entrar():
    while True:
        nome = input("Digite seu Nome: ")
        nick = input("Digite o Login: ")
        senha = input("Digite a Senha: ")
        lista = [str(nome).lower(), str(nick).lower(), str(senha).lower()]
        result = login.buscar(lista)
        if result == True:
            exibir()
            break
        else:
            print("\nUsuário ou Senha inválidos\n")

entrar()
