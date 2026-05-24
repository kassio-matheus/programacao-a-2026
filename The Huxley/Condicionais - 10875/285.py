numero = int(input())

if numero == 0:
    print("NULO")
else:
    par = (numero % 2 == 0)
    positivo = (numero > 0)

    if par == True and positivo == True:
        print("POSITIVO PAR")
    elif par == True and positivo == False:
        print("NEGATIVO PAR")
    elif par == False and positivo == True:
        print("POSITIVO IMPAR")
    elif par == False and positivo == False:
        print("NEGATIVO IMPAR")