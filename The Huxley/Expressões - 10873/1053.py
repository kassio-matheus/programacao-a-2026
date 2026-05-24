pi = 3.14

altura = float(input(""))
raio = float(input(""))

area_cilindro = 2 * pi * raio * altura + 2 * pi * (raio ** 2)
volume_cilindro = pi * (raio ** 2) * altura

print("%.2f" % volume_cilindro)
print("%.2f" % area_cilindro)