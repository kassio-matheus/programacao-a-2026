quantidade = int(input())
array = list(int(i) for i in input().split())

menor_valor = min(array)
posicao = int()

for index in range(0, quantidade):
    if(array[index] == menor_valor):
        posicao = index
        break

print("Menor valor: {}".format(menor_valor))
print("Posicao: {}".format(posicao))