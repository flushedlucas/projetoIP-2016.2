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
            print("\n" + cliente)
            for i, j in enumerate(linhas):
                if j[0] == cliente:
                    print("Comprou %s de %s do vendedor %s" %(j[3],j[2],j[1]))

    elif opcao == str(2):
        vendedor = input("Digite o nome do vendedor: ")
        if vendedor != None:
            arq = open("vendas.txt")
            linhas = arq.readlines()
            arq.close()
            for i, j in enumerate(linhas):
                linhas[i] = j.split(",")
            print("\n" + vendedor)
            for i, j in enumerate(linhas):
                if j[1] == vendedor:
                    print("Vendeu %s de %s para o cliente %s" % (j[3], j[2], j[0]))
    else:
        print("Opcao Invalida")
