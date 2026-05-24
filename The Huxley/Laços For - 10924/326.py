entrada = input().split()
quantidade_linhas = int(entrada[0])
intervalo = int(entrada[1])

numeros = range(1, intervalo + 1)

linha = str()
contagem = int(0)

for i in numeros:
    contagem += 1

    if(i != intervalo and contagem != quantidade_linhas):
        linha = linha + str(numeros[i - 1]) + " "
    else:
        linha = linha + str(numeros[i - 1])

    if(contagem == quantidade_linhas and i != intervalo):
        linha = linha + "\n"
        contagem = 0

    if(i == intervalo):
        print(linha)
        linha = str()