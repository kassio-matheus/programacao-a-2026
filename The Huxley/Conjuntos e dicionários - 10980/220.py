import time
import random

quantidade_alunos = random.randint(1, 10) * 100_000

#Ultilizando conjuntos
start = time.time()

alunos = set()

for i in range(quantidade_alunos):
    numero_matricula = random.randint(1, quantidade_alunos * 10)
    alunos.add(numero_matricula)

end = time.time()

print("Usando conjuntos:")
print(f"Quantidade de alunos inseridos: {quantidade_alunos:,}".replace(",", "."))
print(f"Matrículas únicas comparadas: {len(alunos)}")
print(f"Tempo de execução: {end - start:.4f} segundos")

#Ultilizando listas

start = time.time()

alunos = list()

for i in range(quantidade_alunos // 10):
    numero_matricula = random.randint(1, quantidade_alunos * 10)
    
    if numero_matricula not in alunos:
        alunos.append(numero_matricula)

end = time.time()

print()
print("Usando listas:")
print(f"Quantidade de alunos inseridos: {quantidade_alunos // 10:,}".replace(",", "."))
print(f"Matrículas únicas: {len(alunos)}")
print(f"Tempo de execução: {end - start:.4f} segundos")