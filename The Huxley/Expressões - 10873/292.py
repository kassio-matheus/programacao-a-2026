entrada = input("").split();

a = float(entrada[0]);
b = float(entrada[1]);
c = float(entrada[2]);

pi = 3.14159

area_triangulo = (a * c) / 2;
area_circulo = pi * (c ** 2);
area_trapezio = ((a + b) * c) / 2;
area_quadrado = b ** 2;
area_retangulo = a * b;

print("TRIANGULO:", "%.3f" % area_triangulo);
print("CIRCULO:", "%.3f" % area_circulo);
print("TRAPEZIO:", "%.3f" % area_trapezio);
print("QUADRADO:", "%.3f" % area_quadrado);
print("RETANGULO:", "%.3f" % area_retangulo);