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
