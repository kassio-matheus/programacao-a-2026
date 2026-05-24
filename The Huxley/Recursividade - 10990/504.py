numeros = [int(input()) for _ in range(5)]

def fatorial(n) :
  if n == 0:
    return 1
  else :
    return fatorial(n - 1) * n 

soma = int()

for i in numeros:
    if i % 3 == 0:
        soma += fatorial(i)

print(soma)