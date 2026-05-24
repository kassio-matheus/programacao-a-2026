valor_1 = int(input());
valor_2 = int(input());
valor_3 = int(input());

menor = int();

if valor_1 < valor_2 and valor_1 < valor_3:
    menor = valor_1
elif valor_2 < valor_3:
    menor = valor_2
else:
    menor = valor_3

print(menor)