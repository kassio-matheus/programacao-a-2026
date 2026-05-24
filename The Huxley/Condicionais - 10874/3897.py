tipo = input();
a = float(input());
b = float(input());
c = float(input());

aritmetica = (a + b + c) / 3
harmonica = 3 / (1/a + 1/b + 1/c)
geometrica = (a * b * c) ** (1/3)

if(tipo == "A"):
    print("%.3f" % round(aritmetica, 3))
elif(tipo == "H"):
    print("%.3f" % round(harmonica, 3))
else:
    print("%.3f" % round(geometrica, 3))