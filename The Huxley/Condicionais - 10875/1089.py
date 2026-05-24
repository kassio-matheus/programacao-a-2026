idade = int(input());

infantil_a = [5, 7];
infantil_b = [8, 10];
juvenil_a = [11, 13];
juvenil_b = [14, 17];
adulto = [18, 40];

if(idade >= infantil_a[0] and idade <= infantil_a[1]):
    print("Infantil A")
elif(idade >= infantil_b[0] and idade <= infantil_b[1]):
    print("Infantil B")
elif(idade >= juvenil_a[0] and idade <= juvenil_a[1]):
    print("Juvenil A")
elif(idade >= juvenil_b[0] and idade <= juvenil_b[1]):
    print("Juvenil B")
elif(idade >= adulto[0] and idade <= adulto[1]):
    print("Adulto")
elif(idade >= 41):
    print("Master")
else:
    print("Idade invalida.")