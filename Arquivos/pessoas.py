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
    foto = input("Digite o Foto: ")
    cliente = [nome, endereco, bairro, cidade, cep, estado, telefone, celular, fax, email, rg, cpf, data, foto]
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
    remover = pesquisar(nome, "cliente")
    if remover != None:
        arq = open("cliente.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(" ")
            for x in text:
                if x == remover:
                    text.remove(remover)
        arq = open("cliente.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def removerFornecedor(nome):
    remover = pesquisar(nome, "fornecedor")
    if remover != None:
        arq = open("fornecedor.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(" ")
            for x in text:
                if x == remover:
                    text.remove(remover)
        arq = open("fornecedor.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def removerFuncionario(nome):
    remover = pesquisar(nome, "funcionario")
    if remover != None:
        arq = open("funcionario.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(" ")
            for x in text:
                if x == remover:
                    text.remove(remover)
        arq = open("funcionario.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def consultar_cliente(nome):
    lista = pesquisar(nome, "cliente")
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
        Data de Nascimento: %s
        Foto: %s\n""" % (lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10], lista[11], lista[12], lista[13]))
    else:
        print("Pessoa Nao Encontrada")

def consultar_fornecedor(nome):
    lista = pesquisar(nome, "fornecedor")
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
    lista = pesquisar(nome, "funcionario")
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
    alterar = pesquisar(nome, "cliente")
    if alterar != None:
        novo = montaCliente()
        arq = open("cliente.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(" ")
        for i, j in enumerate(text):
            if i == alterar:
                text[j] = novo
        arq = open("funcionario.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def alterar_fornecedor(nome):
    alterar = pesquisar(nome, "fornecedor")
    if alterar != None:
        novo = montaFornecedor()
        arq = open("fornecedor.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(" ")
        for i, j in enumerate(text):
            if i == alterar:
                text[j] = novo
        arq = open("fornecedor.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def alterar_funcionario(nome):
    alterar = pesquisar(nome, "funcionario")
    if alterar != None:
        novo = montaFuncionario()
        arq = open("funcionario.txt")
        text = arq.readlines()
        arq.close()
        if text != None:
            for i, j in enumerate(text):
                text[j] = i.split(" ")
        for i, j in enumerate(text):
            if i == alterar:
                text[j] = novo
        arq = open("funcionario.txt", "w")
        for t in text:
            for u in t:
                arq.write(u + ",")
            arq.write("\n")
        arq.close()

def adicionar_cliente():
    adiciona = montaCliente()
    arq = open("cliente.txt", "a")
    for i in adiciona:
        arq.write(i + ",")
    arq.write("\n")
    arq.close()

def adicionar_fornecedor():
    adiciona = montaFornecedor()
    arq = open("fornecedor.txt", "a")
    for i in adiciona:
        arq.write(i + ",")
    arq.write("\n")
    arq.close()

def adicionar_funcionario():
    adiciona = montaFuncionario()
    arq = open("funcionario.txt", "a")
    for i in adiciona:
        arq.write(i+",")
    arq.write("\n")
    arq.close()

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
                alterar_cliente(nome)
                if opcao2 == str(1):
                    alterar_cliente()
                    break
                elif opcao2 == str(2):
                    alterar_fornecedor()
                    break
                elif opcao2 == str(3):
                    alterar_funcionario()
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
                if opcao4 == str(1):
                    removerCliente()
                    break
                elif opcao4 == str(2):
                    removerFornecedor()
                    break
                elif opcao4 == str(3):
                    removerFuncionario()
                    break
                else:
                    print("Opcao Invalida")
                    break

        elif opcao == str(5):
            break
        else:
            print("\nOpcao Invalida\n")