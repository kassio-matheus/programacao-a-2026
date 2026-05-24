numero = int(input());
soma = int();

for i in range(numero):
    valor = i

    if(valor % 3 == 0 or valor % 5 == 0):
        soma = soma + valor

print(soma)