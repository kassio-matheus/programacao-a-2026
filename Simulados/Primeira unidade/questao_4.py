entrada_tamanho = input().split()
tamanho_matriz_vertical = int(entrada_tamanho[0])
tamanho_matriz_horizontal = int(entrada_tamanho[1])

nomes = list()
matrizes = list()

#Capturar nomes
for _ in range(tamanho_matriz_vertical):
    nome = input()
    nomes.append(nome)

#Capturar matrizes
for index_vertical in range(tamanho_matriz_vertical):
    valor = input().split()
    matrizes.append([])
    
    for index_horizontal in range(tamanho_matriz_horizontal):
        matrizes[index_vertical].append(int(valor[index_horizontal]))

#Cálculo soma matrizes
somas_totais = list()

for index in range(len(nomes)):
    soma = int()

    for valor in matrizes[index]:
        soma += valor
    
    somas_totais.append(soma)

#Ordenar de forma decrescente (Menor -> Maior) e depois inverter a ordem
def insertion_sort (nomes, somas):
    for index in range(1, len(somas)):
        chave = index
        elemento_anterior = index - 1

        while elemento_anterior >= 0 and somas[chave] < somas[elemento_anterior]:
            somas[elemento_anterior], somas[chave] = somas[chave], somas[elemento_anterior]
            nomes[elemento_anterior], nomes[chave] = nomes[chave], nomes[elemento_anterior]

            chave = elemento_anterior
            elemento_anterior -= 1

insertion_sort(nomes, somas_totais)

nomes = nomes[::-1]
somas_totais = somas_totais[::-1]

for index in range(len(nomes)):
        print(f"{nomes[index]}: {somas_totais[index]}")