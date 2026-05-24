valor = int(input());

soma = float();

numerador = 0
denominador = 0

termos = str();

for i in range(valor):
    numerador = numerador + 1
    denominador = denominador + 3

    termos = ("1/3" if termos == "" else termos + " + {}/{}".format(numerador, denominador))

    soma = soma + (numerador / denominador)

print(termos)
if(soma == 0):
    print("%.2f" % 0.00)
else:
    print("%.2f" % soma)