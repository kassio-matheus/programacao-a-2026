entrada = input().split()
numeros = [int(i) for i in entrada]

maior = numeros[0]

contagem = 0
while numeros[contagem] != 0:
    contagem += 1

    if(maior < numeros[contagem]):
        maior = numeros[contagem]

print(maior)