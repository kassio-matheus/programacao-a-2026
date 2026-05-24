valor_a = int(input())
valor_b = int(input())

def verificar_primo (numero):
    if(numero >= 2):
        primo = True

        for i in range(2, numero):
            if(numero % i == 0):
                primo = False

        return primo
    else:
        return False

def verificar_entradas (valor_a, valor_b):
    if(verificar_primo(valor_a) == False):
        return "O numero {} nao eh primo".format(valor_a)

    if(verificar_primo(valor_b) == False):
        return "O numero {} nao eh primo".format(valor_b)

    if(verificar_primo(valor_a + valor_b)):
        return "A soma de {} e {} eh um primo".format(valor_a, valor_b)
    else:
        return "A soma de {} e {} nao eh um primo".format(valor_a, valor_b)
    
print(verificar_entradas(valor_a, valor_b))