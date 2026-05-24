def somaLista (lista, index=0):
    if index == len(lista):
        return 0
    else:
        return somaLista(lista, index + 1) + lista[index]
    
def somaQtdPares (lista, index=0):
    if index == len(lista):
        return 0
    else:
        if lista[index] % 2 == 0:
            return somaQtdPares(lista, index + 1) + 1
        else:
            return somaQtdPares(lista, index + 1)
        
