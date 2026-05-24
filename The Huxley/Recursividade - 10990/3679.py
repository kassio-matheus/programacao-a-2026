def imprimir_reverso ():
    entrada = int(input())
    
    if(entrada == 0):#caso base
        return 0
    else: #hipótese indutiva
        imprimir_reverso()
        print(entrada)

imprimir_reverso()