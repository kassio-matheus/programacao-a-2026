ano = int(input());

if (ano % 400 == 0):
    print("BISSEXTO")
elif (ano % 100 == 0):
    print("NAOBISSEXTO")
elif (ano % 4 == 0):
    print("BISSEXTO")
else:
    print("NAOBISSEXTO")