def buscar(lista):
    usuarios = [["swameze", "swamy", "1234"],["gilberto", "gil", "5678"],["felipe", "lipe", "1020"]]
    for i in usuarios:
        if lista == i:
            return True
    return False
