entrada = input().split()
intervalo_a = entrada[0]
intervalo_b = entrada[1]

intervalo = (intervalo_b, intervalo_a) if (intervalo_b > intervalo_a) else (intervalo_a, intervalo_b)

multiplos = str()
primeiro = True

for i in range(int(intervalo[0]), int(intervalo[1]) + 1):
    if i % 5 == 0:
        if primeiro == True:
            multiplos += str(i)
            primeiro = False
        else:
            multiplos += "|{}".format(i)

print(multiplos if multiplos != "" else 0)