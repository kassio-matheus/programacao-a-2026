texto = sorted(input(), reverse=True)
repeticoes = dict()

for i in texto:
    if(i in repeticoes):
        caracter = repeticoes.get(i)
        repeticoes.update({i: caracter + 1})
    else:
        repeticoes.update({i: 1})

for i in repeticoes:
    quantidade = repeticoes.get(i)
    print(f"{i} {quantidade}")