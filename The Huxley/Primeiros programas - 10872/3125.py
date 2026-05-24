salario = float(input());
aumento = float(input());

print("Seu salario teve aumento de {}%, passando de R$ {} para R$ {}".format(aumento, salario, (salario * (1 + aumento / 100))));