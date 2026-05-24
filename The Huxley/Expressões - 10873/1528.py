#Volume Esfera = (4πR3)/3

raio = float(input(""));

def calculo (raio) :
    return ((4 * 3.1416 * (raio ** 3)) / 3);

print("%.2f" % calculo(raio));