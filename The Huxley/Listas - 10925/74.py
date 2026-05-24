numeros = [int(input()) for _ in range(100)]
numero_chave = int(input())

for i in range(len(numeros)):
    if(numeros[i] == numero_chave):
        print(i)