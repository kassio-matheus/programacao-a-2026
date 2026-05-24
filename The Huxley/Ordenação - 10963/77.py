qtd_numeros = int(input())
numeros = [int(input()) for _ in range(qtd_numeros)];

# def insertion_sort (lista):
#     for index in range(len(lista)):
#         chave = index
#         elemento_anterior = index - 1

#         while elemento_anterior >= 0 and lista[chave] < lista[elemento_anterior]:
#             lista[chave], lista[elemento_anterior] = lista[elemento_anterior], lista[chave]
#             chave = elemento_anterior
#             elemento_anterior -= 1

#     return lista;

print(*["[{}]".format(i) for i in sorted(numeros)], sep="")