valor_1 = int(input())
valor_2 = int(input())

maior_multiplo = 0
termo = 1

if valor_1 != 0:
    while valor_1 * termo <= valor_2:
        maior_multiplo = valor_1 * termo
        termo += 1

if maior_multiplo == 0:
    print("sem multiplos menores que " + str(valor_2))
else:
    print(maior_multiplo)