quantidade_alunos = int(input())
notas = list(int(input()) for _ in range(quantidade_alunos))

soma = float()
acima_percentual = int()
abaixo_percentual = int()

for i in notas:
    soma += i

media = soma / len(notas)

for i in notas:
    if(i > media and (i * 1.10 > media)):
        acima_percentual += 1
    elif(i < media and ( i* 1.10 < media)):
        abaixo_percentual += 1

print("%.2f" % media)
print(acima_percentual)
print(abaixo_percentual)