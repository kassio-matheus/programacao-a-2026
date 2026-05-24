comprimento_1 = int(input());
comprimento_2 = int(input());
comprimento_3 = int(input());

#Um triângulo isósceles possui pelo menos dois lados de mesma medida e dois ângulos congruentes
#Num triângulo isósceles, o ângulo formado pelos lados congruentes é chamado ângulo do vértice
#Os demais ângulos denominam-se ângulos da base e são congruentes.

#O triângulo equilátero é um caso especial de um triângulo isósceles, que todos os três lados iguais

#Em um triângulo escaleno, as medidas dos três lados são diferentes.
#Os ângulos internos de um triângulo escaleno também possuem medidas diferentes.

if comprimento_1 == comprimento_2 and comprimento_1 == comprimento_3:
    print("equilatero")
elif comprimento_1 != comprimento_2 and comprimento_1 != comprimento_3 and comprimento_2 != comprimento_3:
    print("escaleno")
else:
    print("isosceles")