quantidade_pacientes = int(input())

def risco (pressao, idade):
    if(pressao >= 90 and pressao <= 120 and idade <= 60):
        return "NORMAL"
    elif(pressao > 140 and idade > 60):
        return "ALTO"
    elif(pressao > 140 or idade > 60):
        return "MEDIO"
    elif(pressao > 120):
        return "BAIXO"
    elif(pressao < 90):
        return "CRITICO"
    
resultados = list()

for i in range(quantidade_pacientes):
    nome = input()
    pressao = float(input()) * 10
    idade = int(input())

    resultados.append(f"{nome}: {risco(pressao, idade)}")

for i in resultados:
    print(i)