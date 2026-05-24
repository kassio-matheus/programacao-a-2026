valor_inicial = float(input())
valor_anterior = valor_inicial  # começa com o valor do 1º dia

valor_minimo = 0.50
dias_cumpridos = 0
soma = float(valor_inicial)

for i in range(6):
    novo_valor = float(input())

    if novo_valor >= valor_anterior + valor_minimo:
        dias_cumpridos = dias_cumpridos + 1

    valor_anterior = novo_valor  # atualiza para o próximo dia
    soma = soma + novo_valor

print("R$", "%.2f" % soma, sep="")
print(dias_cumpridos)