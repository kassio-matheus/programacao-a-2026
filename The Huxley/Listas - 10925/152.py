quantidade_numeros = int(input())
entrada = input().split()
numeros = [int(entrada[i]) for i in range(quantidade_numeros)]

print(' '.join(str(n) for n in numeros[::-1]))
print(' '.join(str(n) for n in numeros[1:] + numeros[:1]))
print(' '.join(str(n) for n in sorted(numeros, reverse=True)))