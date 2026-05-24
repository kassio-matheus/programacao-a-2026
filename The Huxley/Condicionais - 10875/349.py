mes = int(input())
ano = int(input())

def verificar_bissexto (ano):
    if(ano % 400 == 0):
        return True
    elif(ano % 100 == 0):
        return False
    elif(ano % 4 == 0):
        return True
    else:
        return False;

mes_30 = [4, 6, 9, 11];

if(verificar_bissexto(ano) and mes == 2):
    print(29)
elif (mes == 2):
    print(28)
elif mes in mes_30:
    print(30)
else:
    print(31)