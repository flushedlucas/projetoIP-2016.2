from Arquivos import login, pessoas, estoque, vendas
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

def entrar():
    while True:
        nome = input("Digite seu Nome: ")
        senha = input("Digite a Senha: ")
        lista = [str(nome).lower(), str(senha).lower()]
        result = login.buscar(lista)
        if result == True:
            exibir()
            break
        else:
            print("\nUsuário ou Senha inválidos\n")

entrar()
