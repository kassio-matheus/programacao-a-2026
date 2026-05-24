valor = int(input(""));

def calcular_cedulas(valor, denominacao):
    if valor >= denominacao:
        return (valor // denominacao, valor % denominacao)
    return (0, valor)

def calculo_geral(valor):
    print(valor)

    qtd100, valor = calcular_cedulas(valor, 100)
    qtd50,  valor = calcular_cedulas(valor, 50)
    qtd20,  valor = calcular_cedulas(valor, 20)
    qtd10,  valor = calcular_cedulas(valor, 10)
    qtd5,   valor = calcular_cedulas(valor, 5)
    qtd2,   valor = calcular_cedulas(valor, 2)
    qtd1,   valor = calcular_cedulas(valor, 1)

    print(str(qtd100) + " nota(s) de R$ 100,00")
    print(str(qtd50)  + " nota(s) de R$ 50,00")
    print(str(qtd20)  + " nota(s) de R$ 20,00")
    print(str(qtd10)  + " nota(s) de R$ 10,00")
    print(str(qtd5)   + " nota(s) de R$ 5,00")
    print(str(qtd2)   + " nota(s) de R$ 2,00")
    print(str(qtd1)   + " nota(s) de R$ 1,00")

calculo_geral(valor);