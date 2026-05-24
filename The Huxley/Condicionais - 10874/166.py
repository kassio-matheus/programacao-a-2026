valor = int(input(""))

algarimos = list(str(valor))

if (algarimos[0] == "-"):
    print(-int(algarimos[-1]))
else:
    print(int(algarimos[-1]))