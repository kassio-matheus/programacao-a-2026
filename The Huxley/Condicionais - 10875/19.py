nota_1 = float(input());
nota_2 = float(input());
nota_3 = float(input());

media = (nota_1 + nota_2 + nota_3) / 3;

if(media >= 7):
    print("aprovado")
elif (3 <= media < 7):
    print("prova final")
else:
    print("reprovado")