entrada = input().split()

investimento_inicial = float(entrada[0])
taxa_trimestral = float(entrada[1])
periodo_investimento_trimestres = int((int(entrada[2]) * 12) / 3)

montante = float(investimento_inicial)

for i in range(periodo_investimento_trimestres):
    rendimento = montante * taxa_trimestral
    montante = montante * (1 + taxa_trimestral)
    print("Rendimento:", "%.2f" % round(rendimento, 2), "Montante:", "%.2f" % round(montante, 2))