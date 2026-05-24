casos_teste = int(input())

def contar_vogais (frase, vogais):
    contador = int()
    for palavra in frase:
        for letra in palavra:
             if(letra in vogais):
                  contador += 1

    return contador

for _ in range(casos_teste):
        vogais = list(input())
        frase = input().split()

        print(contar_vogais(frase, vogais))