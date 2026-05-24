import random
import time

numeros = random.sample(range(100),20)

def selection_sort (lista):
    for index in range(0, len(lista)):
        menor_indice = index
        
        for item in range(index, len(lista)):
            if(lista[item] < lista[menor_indice]):
                menor_indice = item
        
        lista[index], lista[menor_indice] = lista[menor_indice], lista[index]

    return lista;

tempo_inicial = time.perf_counter()
print(selection_sort(numeros))
tempo_final = time.perf_counter()
print(f"Tempo de processamento: {tempo_final - tempo_inicial:.6f} segundos")