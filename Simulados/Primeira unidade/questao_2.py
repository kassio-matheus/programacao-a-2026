entrada = int(input())

rapidas = int(0)
medias = int(0)
longas = int(0)
total = int(0)

def calcular_tempo_cirurgia (tempo):
    if(tempo <= 30):
        return "RAPIDA"
    elif(tempo > 30 and tempo <= 90):
        return "MEDIA"
    elif(tempo > 90):
        return "LONGA"

while entrada != 0:
    total += entrada
    resultado = calcular_tempo_cirurgia(entrada)

    if(resultado == "RAPIDA"):
        rapidas += 1
    elif(resultado == "MEDIA"):
        medias += 1
    elif(resultado == "LONGA"):
        longas += 1

    entrada = int(input())

print(f"RAPIDAS: {rapidas}")
print(f"MEDIAS: {medias}")
print(f"LONGAS: {longas}")
print(f"TOTAL: {total}")

if(total != 0):
    print(f"MEDIA: {"%.1f" % (total / (rapidas + medias + longas))}")
else:
    print("MEDIA: 0.0")