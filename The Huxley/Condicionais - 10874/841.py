valor_1 = float(input(""));
valor_2 = float(input(""));
valor_3 = float(input(""));

media = (valor_1 + valor_2 + valor_3) / 3;
qtd = int();

if(valor_1 > media):
    qtd = qtd + 1;

if(valor_2 > media):
    qtd = qtd + 1;

if(valor_3 > media):
    qtd = qtd + 1;

print(qtd)