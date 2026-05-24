entrada = input().split()
numeros = list(int(entrada[i]) for i in range(10))
contagem = int()

for i in numeros:
    numero_chave = numeros[9]

    if(i == numero_chave):
        contagem += 1

print("O numero {} apareceu {} vezes".format(numeros[9], contagem))