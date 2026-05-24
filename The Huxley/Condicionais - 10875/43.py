valor_1 = int(input());
valor_2 = int(input());
valor_3 = int(input());

if(valor_1 == valor_2 and valor_1 == valor_3):
    print(1)
elif((valor_1 != valor_2 and valor_1 == valor_3) or (valor_1 == valor_2 and valor_1 != valor_3)):
    print(3)
else:
    print(2)