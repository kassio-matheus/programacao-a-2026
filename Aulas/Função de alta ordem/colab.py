#Programa para calcular a área de um retângulo dados os comprimentos de duas arestas
def calcular_area_retangulo (a: float, b: float):
    return a * b

retangulo = calcular_area_retangulo

#print(f"{retangulo(2, 2)} m²")

#Programa para calcular a área de uma circunferência dado o valor do raio.

def calcular_area_circunferencia (raio):
    area = raio ** 2 * 3.14
    return area

circunferencia = calcular_area_circunferencia

#print(f"{circunferencia(2)} m²")

#Programa para determinar se três valores passados podem representar um triângulo ou não.

def validador_triangulo (a, b, c):
    teste_a = lambda a, b, c: True if (a + b) > c else False
    teste_b = lambda a, b, c: True if (a + c) > b else False
    teste_c = lambda a, b, c: True if (c + b) > a else False

    if (teste_a(a, b, c) and teste_b(a, b, c) and teste_c(a, b, c)):
        return True
    else:
        return False
    
triangulo_1 = validador_triangulo
triangulo_2 = validador_triangulo

#print(triangulo_1(3, 4, 5))
#print(triangulo_2(20, 7, 8))

#Programa para classificar um triângulo em Equilátero, Isósceles ou Escaleno a partir dos valores de
#seus três lados.

#Apenas com cidadãs de alta classe
def tipo_triangulo (a, b, c):
    equilatero = lambda a, b, c: True if (a == b and a == c and b == c) else False
    escaleno = lambda a, b, c: True if (a != b and a != c and b != c) else False

    if(equilatero(a, b, c)):
        return "Equilatéro"
    elif (escaleno(a, b, c)):
        return "Escaleno"
    else:
        return "Isósceles"

triangulo = tipo_triangulo

#print(triangulo(1, 3, 2))

#Ultilizando funções de alta ordem

def obter_func(tipo):
    if tipo == "verificar_escaleno":
        return lambda a, b, c: a != b and a != c and b != c
    elif tipo == "verificar_equilatero":
        return lambda a, b, c: a == b and a == c and b == c

def tipo_triangulo(a, b, c):
    equilatero = obter_func("verificar_equilatero")
    escaleno = obter_func("verificar_escaleno")

    if equilatero(a, b, c):
        return "Equilátero"
    elif escaleno(a, b, c):
        return "Escaleno"
    else:
        return "Isósceles"
    
#print(triangulo(1, 3, 2))

#Programa para calcular a distância euclidiana entre dois pontos [(x1,y1),(x2,y2)] no plano cartesiano.
#Utilize a equação geral da reta para calcular a distância quando a reta não for paralela a nenhum dos
#eixos (abscissas ou ordenadas) e as versões simplificadas quando for paralela.

#pontos = [{"x1": int(input()), "y1": int(input())}, {"x2": int(input()), "y2": int(input())}]

def raiz (num):
    return num ** 0.5

def calcular_distancia (raiz):
    def diferenca (p1, p2):
        dx = p2["x2"] - p1["x1"]
        dy = p2["y2"] - p1["y1"]

        return raiz(dx**2 + dy**2)
    
    return diferenca

diferenca = calcular_distancia(raiz)

#print(diferenca(pontos[0], pontos[1]))

def menor_valor (a, b):
    return a if a <= b else b
    
def calcular_menor_valor (menor_valor):
    def comparar (a, b, c):
        return menor_valor(c, menor_valor(a, b))
    
    return comparar

comparacao = calcular_menor_valor(menor_valor)
print(comparacao(1, 2, 3))