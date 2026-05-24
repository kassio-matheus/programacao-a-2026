valor_1 = int(input())
valor_2 = int(input())

soma = int(0);

intervalo = (valor_1, valor_2 + 1) if valor_1 < 0 else ( valor_2, valor_1 + 1);

print(intervalo)

for i in range(intervalo[0], intervalo[1]):
    if(i > 0):
        soma += i

print(soma)