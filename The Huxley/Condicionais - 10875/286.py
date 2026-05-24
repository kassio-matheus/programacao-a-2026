alice = int(input());
beto = int(input());
clara = int(input());

if((alice != beto and alice != clara) and (beto == clara)):
    print("A")
elif((beto != alice and beto != alice) and (alice == clara)):
    print("B")
elif((clara != alice and clara != beto) and (alice == beto)):
    print("C")
else:
    print("*")