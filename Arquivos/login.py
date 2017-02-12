def buscar(lista):
    usuarios = [["swameze", "1234"],["gilberto", "5678"],["felipe", "1020"]]
    for i in usuarios:
        if lista == i:
            return True
    return False
