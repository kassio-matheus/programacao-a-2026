quantidade_medicoes = int(input())

medicoes = list()

total_temperaturas = float()
media = float()

febre = int()
hiportemia = int()

for index in range(quantidade_medicoes):
    temperatura = float(input())
    medicoes.append(temperatura)

    if(temperatura > 37.5):
        febre += 1
    elif(temperatura < 36.0):
        hiportemia += 1

    total_temperaturas += temperatura

    if(index == quantidade_medicoes - 1):
        media = total_temperaturas / len(medicoes)

print(f"MEDIA: {"%.2f" % media}")
print(f"FEBRE: {febre}")
print(f"HIPORTEMIA: {hiportemia}")
print(f"PRIMEIRAS: {medicoes[0:3]}")
print(f"INVERSA: {medicoes[::-1]}")