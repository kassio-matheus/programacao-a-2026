distancia_total = float(input(""));
total_combustivel = float(input(""));

autonomia = distancia_total / total_combustivel;

print("%.3f" % autonomia, "km/l");