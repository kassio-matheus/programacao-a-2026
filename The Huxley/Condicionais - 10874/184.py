diametro = float(input());

dimensoes = input().split();
altura = int(dimensoes[0]);
largura = int(dimensoes[1]);
profundidade = int(dimensoes[0]);

#Contendo a letra 'S' caso a bola de boliche caiba dentro da caixa ou 'N' caso contrário.

if(diametro <= altura and diametro <= largura and diametro <= profundidade):
    print("S")
else:
    print("N")