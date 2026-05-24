segundos = int(input(""));

horas = segundos // 3600;
minutos = (segundos % 3600) // 60;
segundos_resto = segundos % 60

print("%.0f" % horas, ":", "%.0f" % round(minutos, 1), ":", "%.0f" % segundos_resto)