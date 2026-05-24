numeros = [7, 1, 2, 3, 5, 6, 4]

def selection_sort (lista):
    for index in range(0, len(lista)):
        menor_indice = index

        for i in range(index, len(lista)):
            if(lista[i] < lista[menor_indice]):
                menor_indice = i

        lista[index], lista[menor_indice] = lista[menor_indice], lista[index]

    return lista;
print(selection_sort(numeros))