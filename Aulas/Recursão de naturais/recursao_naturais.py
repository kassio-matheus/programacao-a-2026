def multiplica_por_n (m, n):
    if(m == 0):
        return 0
    else:
        return multiplica_por_n(m - 1, n) + n #Só retorna no caso base: 0
        #1 (5 - 1, 3) + 3
        #2 (4 - 1, 3) + 3
        #3 (3 - 1, 3) + 3
        #4 (2 - 1, 3) + 3
        #5 (1 - 1, 3): 0 (caso base) -> 12 + 3
        #(3 + 3 + 3 + 3) + 3

def multiplica_por_m (m, n):
    if(n == 0):
        return 0
    else:
        return multiplica_por_m(n - 1, m) + m #Só retorna no caso base: 0
        #1 (3 - 1, 5) + 5
        #2 (2 - 1, 5) + 5
        #3 (1 - 1, 5): 0 (caso base) -> 10 + 5
        #(5 + 5) + 5


#5! = 5 * 4 * 3 * 2 * 1
def fatorial(n) :
  if n == 0:
    return 1
  else :
    return fatorial(n - 1) * n 

# m = base
# n = expoente
def exponenciacao (m, n):
    if n == 0:
      return 1
    else:
      return exponenciacao(m, n - 1) * m

def soma_cubos(n):
    if n == 1:
        return 1
    else:
        return soma_cubos(n - 1) + n**3
    

def soma_fracao_fatorial (n, d):
    print(n, d)
    if n / d == 1:
      return 1
    else:
      return soma_fracao_fatorial(n, d - 1) + (n / fatorial(d))

#1 (1, 3) = 1/6
#2 (1, 2) = 1/2
#3 (1, 1) = 1 (caso base)
# (1 + 1/2) + 1/6
def imprimir1Ate(n) :
  if n >= 1 :
    imprimir1Ate(n-1)
    print(n)


#m = asteriscos verticais
#n = asteriscos horizontais
def imprimeRetangulo (m, n):
    if m == 1:
       return "*" * n
    else:
       return imprimeRetangulo(m - 1, n) + "\n" + "*" * n

def imprimeTriangulo (n):
    if n == 1:
       return "*"
    else:
       return imprimeTriangulo(n - 1) + "\n" + "*" * n

#m = base superior
#n = base inferior
def imprimeTrapezio (m, n):
    if(m > n): return

    if m == n:
       return "*" * m
    else:
       return imprimeTrapezio(m, n - 1) + "\n" + "*" * n