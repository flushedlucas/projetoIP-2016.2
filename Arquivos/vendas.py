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
        arq.close()
        for i,j in enumerate(linhas):
            linhas[i] = j.split(",")
        for i, j in enumerate(linhas):
            pass

    elif opcao == str(2):
        arq = open("vendas.txt")
        linhas = arq.readlines()
        arq.close()
        for i, j in enumerate(linhas):
            linhas[i] = j.split(",")
        for i, j in enumerate(linhas):
            pass
    else:
        print("Opcao Invalida")
