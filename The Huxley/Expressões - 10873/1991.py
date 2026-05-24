#Sabe-se que o Kwh de uma residência custa R$ 1,50. Faça um programa em Python que receba a quantidade de KWh consumidos, calcule e mostre:
#a) O valor a ser pago pela residência
#b) O valor a ser pago com desconto de 15%

horas = float(input(""));
kwh = horas * 1.50;
desconto = kwh * 0.85;

print("Valor a ser pago: R$ {} reais".format("%.2f" % kwh))
print("Valor a ser pago com desconto: R$ {} reais".format("%.2f" % desconto))