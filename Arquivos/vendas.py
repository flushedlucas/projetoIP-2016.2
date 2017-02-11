from Arquivos import estoque
def comprar():
    nome = input("Digite o nome do produto: ")
    if nome != None:
        produto = estoque.pesquisar(nome)
        fornecedor = input("Digite o nome do fornecedor: ")
        if fornecedor != None:
            funcionario = input("Digite o nome do Funcionario: ")
            if funcionario != None:
                apv = estoque.comprar(produto)
                if apv != None:
                    arq = open("compras.txt", "a")
                    arq.writeline([produto, funcionario, fornecedor])
                    arq.close()

def vender():
    nome = input("Digite o nome do produto: ")
    if nome != None:
        produto = estoque.pesquisar(nome)
        cliente = input("Digite o nome do cliente: ")
        if cliente != None:
            vendedor = input("Digite o nome do vendedor: ")
            if vendedor != None:
                apv = estoque.vender(produto)
                if apv != None:
                    arq = open("vendas.txt", "a")
                    arq.writeline([produto, vendedor, cliente])
                    arq.close()

def relatorio():
    print("""
            Vendas

                1 - Por Cliente
                2 - Por Vendedor

            """)
    opcao = input("Digite a opcao: ")
    if opcao == str(1):
        arq = open("vendas.txt")
        linhas = arq.readlines()

    elif opcao == str(2):
        pass
    else:
        print("Opcao Invalida")