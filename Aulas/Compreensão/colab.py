matriz = [1, 2, 3, [4, 5], [[6, 7]], [[[8]]], [[[[[[[[[9]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]]
n1 = [num for item in matriz for num in (item if isinstance(item, list) else [item])]
#print(n1)

n2 = [num for item in n1 for num in (item if isinstance(item, list) else [item])]
#print(n2)

n3 = [num for item in n2 for num in (item if isinstance(item, list) else [item])]
#print(n3)

def recursao (lista, index: int):
    if(index >= len(lista)):
        return []
    else:
        if(isinstance(lista[index], int)):
            return [lista[index]] + recursao(lista, index + 1)
        elif(isinstance(lista[index], list)):
            return recursao(lista[index], 0) + recursao(lista, index + 1)
        
print(recursao(matriz, index=0))