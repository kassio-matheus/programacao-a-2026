numeros_apostas = int(input())
apostas = [[int(i) for i in input().split(",")] for _ in range(numeros_apostas)]
resultado = set(int(i) for i in input().split())
ganhadores = int()

for item in apostas:
    aposta = set(item)

    if(len(aposta.intersection(resultado)) >= 6):
        ganhadores += 1

print("Total de ganhadores:", ganhadores)