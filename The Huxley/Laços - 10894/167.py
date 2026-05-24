alibaba = 0
alcapone = 0
brancos = 0
nulos = 0

vencedor = 0

while True:
    try:
        voto = int(input())
    except EOFError: # Caso o input termine inesperadamente
        break

    if voto == 83:
        alibaba += 1
    elif voto == 93:
        alcapone += 1
    elif voto == 0:
        brancos += 1
    elif voto == -1:
        # Lógica de desempate e vencedor
        if alibaba >= alcapone: # Se houver empate, Alibaba vence conforme sua regra
            vencedor = 83
        else:
            vencedor = 93
        break
    else:
        nulos += 1

# Cálculo da porcentagem corrigido
votos_totais = alibaba + alcapone + brancos

if votos_totais > 0:
    # A fórmula correta: (votos / total) * 100
    percentual_alibaba = (alibaba / votos_totais) * 100
    percentual_alcapone = (alcapone / votos_totais) * 100
else:
    percentual_alibaba = 0.0
    percentual_alcapone = 0.0

print(alibaba)
print(alcapone)
print(brancos)
print(nulos)
print(vencedor)
print("%.2f" % percentual_alibaba)
print("%.2f" % percentual_alcapone)