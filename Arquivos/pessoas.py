def montaCliente():
    nome = input("Digite o Nome: ")
    endereco = input("Digite o Endereço: ")
    bairro = input("Digite o Bairro: ")
    cidade = input("Digite o Cidade: ")
    cep = input("Digite o CEP: ")
    estado = input("Digite o Estado: ")
    telefone = input("Digite o Telefone: ")
    celular = input("Digite o Celular: ")
    fax = input("Digite o Fax: ")
    email = input("Digite o Email: ")
    rg = input("Digite o RG: ")
    cpf = input("Digite o CPF/CNPJ: ")
    data = input("Digite o Data de Nascimento: ")
    cliente = [nome, endereco, bairro, cidade, cep, estado, telefone, celular, fax, email, rg, cpf, data]
    return cliente

def montaFornecedor():
    nome = input("Digite o Nome: ")
    cpf = input("Digite o CPF/CNPJ: ")
    contato = input("Digite o contato: ")
    endereco = input("Digite o Endereço: ")
    bairro = input("Digite o Bairro: ")
    cidade = input("Digite o Cidade: ")
    estado = input("Digite o Estado: ")
    cep = input("Digite o CEP: ")
    telefone = input("Digite o Telefone: ")
    celular = input("Digite o Celular: ")
    fax = input("Digite o Fax: ")
    fornecedor = [nome, cpf, contato, endereco, bairro, cidade, estado, cep, telefone, celular, fax]
    return fornecedor

def montaFuncionario():
    nome = input("Digite o Nome: ")
    cargo = input("Digite o Cargo: ")
    data = input("Digite o Data de Nascimento: ")
    sexo = input("Digite o Sexo: ")
    endereco = input("Digite o Endereco: ")
    bairro = input("Digite o Bairro: ")
    cidade = input("Digite o Cidade: ")
    cep = input("Digite o CEP: ")
    estado = input("Digite o Estado: ")
    telefone = input("Digite o Telefone: ")
    celular = input("Digite o Celular: ")
    funcionario = [nome, cargo, data, sexo, endereco, bairro, cidade, cep, estado, telefone, celular]
    return funcionario

def pesquisar(nome, opcao):
    nome = nome.lower()
    arq = open(opcao + ".txt")
    text = arq.readlines()
    arq.close()
    if text != None:
        for i, j in enumerate(text):
            text[i] = j.split(",")
        for x in text:
            if x[0].lower() == nome:
                return x
    return None

def removerCliente(nome):
    remover = pesquisar(nome, "clientes")
    if remover != None:
        arq = open("clientes.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[i] = j.split(",")
            for x in text:
                if x == remover:
                    resposta = procuraCliente(remover[0])
                    if resposta == False:
                        text.remove(remover)
                    else:
                        print("\n\nNao se pode remover um cliente que já tenha efetuado alguma compra. \n\n")
        arq = open("clientes.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def removerFornecedor(nome):
    remover = pesquisar(nome, "fornecedores")
    if remover != None:
        arq = open("fornecedores.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[i] = j.split(",")
            for x in text:
                if x == remover:
                    text.remove(remover)
        arq = open("fornecedores.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def removerFuncionario(nome):
    remover = pesquisar(nome, "funcionarios")
    if remover != None:
        arq = open("funcionarios.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[i] = j.split(",")
            for x in text:
                if x == remover:
                    resposta = procuraVendedor(remover[0])
                    if resposta == False:
                        text.remove(remover)
                    else:
                        print("\n\nNao se pode remover um vendedor que já tenha vendido um produto. \n\n")
        arq = open("funcionarios.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def consultar_cliente(nome):
    lista = pesquisar(nome, "clientes")
    if lista != None:
        print("""
        Nome: %s
        Endereço: %s
        Bairro: %s
        Cidade: %s
        CEP: %s
        Estado: %s
        Telefone: %s
        Celular: %s
        Fax: %s
        Email: %s
        RG: %s
        CPF/CNPJ: %s
        Data de Nascimento: %s\n""" % (lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10], lista[11], lista[12]))
    else:
        print("Pessoa Nao Encontrada")

def consultar_fornecedor(nome):
    lista = pesquisar(nome, "fornecedores")
    if lista != None:
        print("""Nome: %s
        CPF/CNPJ: %s
        Contato: %s
        Endereço: %s
        Bairro: %s
        Cidade: %s
        Estado: %s
        CEP: %s
        Telefone: %s
        Celular: %s
        Fax: %s""" % (lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10]))
        return
    print("Pessoa Nao Encontrada")

def consultar_funcionario(nome):
    lista = pesquisar(nome, "funcionarios")
    if lista != None:
        print("""Nome: %s
        Cargo: %s
        Data: %s
        Sexo: %s
        Endereço: %s
        Bairro: %s
        Cidade: %s
        CEP: %s
        Estado: %s
        Telefone: %s
        Celular: %s""" % (lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10]))
        return
    print("Pessoa Nao Encontrada")

def alterar_cliente(nome):
    alterar = pesquisar(nome, "clientes")
    if alterar != None:
        novo = montaCliente()
        arq = open("clientes.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[i] = j.split(",")
        for i, j in enumerate(text):
            if j == alterar:
                text[i] = novo
        arq = open("clientes.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def alterar_fornecedor(nome):
    alterar = pesquisar(nome, "fornecedores")
    if alterar != None:
        novo = montaFornecedor()
        arq = open("fornecedores.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[i] = j.split(",")
        for i, j in enumerate(text):
            if j == alterar:
                text[i] = novo
        arq = open("fornecedores.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def alterar_funcionario(nome):
    alterar = pesquisar(nome, "funcionarios")
    if alterar != None:
        novo = montaFuncionario()
        arq = open("funcionarios.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[i] = j.split(",")
        for i, j in enumerate(text):
            if j == alterar:
                text[i] = novo
        arq = open("funcionarios.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def adicionar_cliente():
    adiciona = montaCliente()
    arq = open("clientes.txt", "a")
    for i in adiciona:
        arq.write(i + ",")
    arq.write("\n")
    arq.close()

def adicionar_fornecedor():
    adiciona = montaFornecedor()
    arq = open("fornecedores.txt", "a")
    for i in adiciona:
        arq.write(i + ",")
    arq.write("\n")
    arq.close()

def adicionar_funcionario():
    adiciona = montaFuncionario()
    arq = open("funcionarios.txt", "a")
    for i in adiciona:
        arq.write(i+",")
    arq.write("\n")
    arq.close()

def procuraCliente(cliente):
    arq = open("vendas.txt")
    text = arq.readlines()
    arq.close()
    if text != None:
        for i, j in enumerate(text):
            text[i] = j.split(",")
        for i in text:
            if i[0] == cliente:
                return True
            else:
                return False

def procuraVendedor(vendedor):
    arq = open("vendas.txt")
    text = arq.readlines()
    arq.close()
    if text != None:
        for i, j in enumerate(text):
            text[i] = j.split(",")
        for i in text:
            if i[1] == vendedor:
                return True
            else:
                return False

def iniciar():
    while True:
        print("""
                Cadastro

                    1 - Adicionar
                    2 - Alterar
                    3 - Consultar
                    4 - Remover
                    5 - Voltar

                     """)
        opcao = input("Opção: ")
        if opcao == str(1):
            while True:
                print("""\n\n
                    Adicionar

                    1 - Cliente
                    2 - Fornecedor
                    3 - Funcionario

                    """)
                opcao1 = input("Opcao: ")
                if opcao1 == str(1):
                    adicionar_cliente()
                    break
                elif opcao1 == str(2):
                    adicionar_fornecedor()
                    break
                elif opcao1 == str(3):
                    adicionar_funcionario()
                    break
                else:
                    print("Opcao Invalida")
                    break
        elif opcao == str(2):
            while True:
                print("""
                    Alterar

                    1 - Cliente
                    2 - Fornecedor
                    3 - Funcionario

                    """)
                opcao2 = input("Opcao: ")
                nome = input("Digite o nome: ")
                if opcao2 == str(1):
                    alterar_cliente(nome)
                    break
                elif opcao2 == str(2):
                    alterar_fornecedor(nome)
                    break
                elif opcao2 == str(3):
                    alterar_funcionario(nome)
                    break
                else:
                    print("Opcao Invalida")
                    break
        elif opcao == str(3):
            while True:
                print("""
                    Consultar

                    1 - Cliente
                    2 - Fornecedor
                    3 - Funcionario

                    """)
                opcao3 = input("Opcao: ")
                nome = input("Digite o nome: ")
                if opcao3 == str(1):
                    consultar_cliente(nome)
                    break
                elif opcao3 == str(2):
                    consultar_fornecedor(nome)
                    break
                elif opcao3 == str(3):
                    consultar_funcionario(nome)
                    break
                else:
                    print("Opcao Invalida")
                    break
        elif opcao == str(4):
            while True:
                print("""
                    Remover

                    1 - Cliente
                    2 - Fornecedor
                    3 - Funcionario

                    """)
                opcao4 = input("Opcao: ")
                nome = input("Digite o nome: ")
                if opcao4 == str(1):
                    removerCliente(nome)
                    break
                elif opcao4 == str(2):
                    removerFornecedor(nome)
                    break
                elif opcao4 == str(3):
                    removerFuncionario(nome)
                    break
                else:
                    print("Opcao Invalida")
                    break

        elif opcao == str(5):
            break
        else:
            print("\nOpcao Invalida\n")