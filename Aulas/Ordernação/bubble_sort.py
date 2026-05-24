import random
import time

numeros = random.sample(range(100), 20)

def bubble_sort (lista):
    for _ in range (len(lista) - 1):
        for index in range(len(lista) - 1):
            if(lista[index] > lista[index + 1]):
                lista[index], lista[index + 1] = lista[index + 1], lista[index]

    return lista;

tempo_inicial = time.perf_counter()
print(bubble_sort(numeros))
tempo_final = time.perf_counter()
print(f"Tempo de processamento: {tempo_final - tempo_inicial:.6f} segundos")