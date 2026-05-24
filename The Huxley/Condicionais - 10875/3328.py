consumo = int(input());

valor_total = float();
kwh = float();

if(consumo <= 99):
    kwh = 1.35
    valor_total = kwh * consumo
elif(consumo <= 299):
    kwh = 1.55
    valor_total = kwh * consumo
elif(consumo <= 574):
    kwh = 1.75
    valor_total = (kwh * consumo) * (1.10 if consumo > 300 else 1)  
else:
    kwh = 2.15
    valor_total = (kwh * consumo) * 1.10

if(valor_total < 35):
    print("%.2f" % 35.00);
else:
    print("%.2f" % valor_total);

print("%.2f" % kwh);