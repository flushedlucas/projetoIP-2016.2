def relatorio():
    print("""
            Vendas

                1 - Por Cliente
                2 - Por Vendedor

            """)
    opcao = input("Digite a opcao: ")
    if opcao == str(1):
        cliente = input("Digite o nome do cliente: ")
        if cliente != None:
            arq = open("vendas.txt")
            linhas = arq.readlines()
            arq.close()
            for i,j in enumerate(linhas):
                linhas[i] = j.split(",")
            print("\nCliente: " + cliente)
            for i, j in enumerate(linhas):
                if j[0] == cliente:
                    print("""
                    Produto: %s
                    Quantidade: %s
                    Vendedor %s
                    """ %(j[2],j[3],j[1]))

    elif opcao == str(2):
        vendedor = input("Digite o nome do vendedor: ")
        if vendedor != None:
            arq = open("vendas.txt")
            linhas = arq.readlines()
            arq.close()
            for i, j in enumerate(linhas):
                linhas[i] = j.split(",")
            print("\nVendedor: " + vendedor)
            for i, j in enumerate(linhas):
                if j[1] == vendedor:
                    print("""
                    Produto: %s
                    Quantidade: %s
                    Cliente: %s
                    """ % (j[2], j[3], j[0]))
    else:
        print("Opcao Invalida")
