quantidade_participantes = int(input())
participantes = dict()

for i in range(quantidade_participantes):
    entrada = input().split()
    nome = entrada[0]
    presentes = set({entrada[1], entrada[2], entrada[3]})

    participantes.update({nome: presentes})

entrada = input().split()

while entrada[0] != "FIM":
    participante = entrada[0]
    presente = entrada[1]

    if(presente in participantes.get(participante)):
        print("Uhul! Seu amigo secreto vai adorar")
    else:
        print("Tente Novamente!")

    entrada = input().split()