valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())

array = [valor_1, valor_2, valor_3]
ordem = "CRESCENTE" #Crescente, Decrescente, Não existe

for index in range(len(array)):
    if(index == 0 and array[index] % 2 != 0):
        ordem = "Decrescente"
    
    if(array[index] < 0):
        ordem = "Não existe"
        print("Ordenacao cancelada.")
        break

if(ordem == "CRESCENTE"):
    array = sorted(array, reverse=True)
elif(ordem == "Decrescente"):
    array = sorted(array)

if(ordem != "Não existe"):
    for i in array:
        print(i)