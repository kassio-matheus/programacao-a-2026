quantidade_indices = int(input())
percentuais_candidato = list([float(i) for i in input().split()])
percentuais_concorrente = list([float(i) for i in input().split()])

maior_diferenca = float()

for i in range(quantidade_indices):
    valor_a = percentuais_candidato[i]
    valor_b = percentuais_concorrente[i]

    if((valor_a > valor_b) and (valor_a - valor_b) > maior_diferenca):
        maior_diferenca = valor_a - valor_b

print("%.2f" % maior_diferenca)