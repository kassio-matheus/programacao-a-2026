# Escreva a funcao interseccao(lista1, lista2) abaixo:
def interseccao(lista1, lista2):
	lista1 = set(lista1)
	lista2 = set(lista2)
	
	return sorted(list(lista1.intersection(lista2)))

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista1 = set(eval(input()))
lista2 = set(eval(input()))
resultado = interseccao(lista1, lista2)

if isinstance(resultado, list):
	print(resultado)
else:
	print("Erro. Voce deve devolver uma lista")