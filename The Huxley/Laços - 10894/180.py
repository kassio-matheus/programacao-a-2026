entrada_1 = input().split();
numero_leituras = int(entrada_1[0]); #Sensor por andar
capacidade = int(entrada_1[1]); #Capacidade máxima

#S para capacidade excedida e N para capacidade normal

pessoas_elevador = int(0);

for i in range(numero_leituras):
    entrada_2 = input().split();
    saidas = int(entrada_2[0]); #Saidas por andar
    entradas = int(entrada_2[1]); #Entradas por andar

    pessoas_elevador += entradas - saidas;
