valor_1 = int(input());
valor_2 = int(input());
contagem = 0;

valor_atual = valor_1;

while contagem <= (valor_2 - valor_1):
    contagem += 1;

    if(valor_atual % 2 != 0):
        print(valor_atual)
    
    valor_atual += 1