import random
import time

numeros = random.sample(range(100), 20)

def insertion_sort (lista):
    for index in range(1, len(lista)):
        chave = index #elemento a ser comparado sempre com a esquerda
        elemento_anterior = chave - 1
 
        while lista[chave] < lista[elemento_anterior] and elemento_anterior >= 0:
            lista[chave], lista[elemento_anterior] = lista[elemento_anterior], lista[chave]
            chave = elemento_anterior
            elemento_anterior -= 1

    return lista

tempo_inicial = time.perf_counter()
print(insertion_sort(numeros))
tempo_final = time.perf_counter()
print(f"Tempo de processamento: {tempo_final - tempo_inicial:.6f} segundos")