tempo = int(input("Quanto tempo para analisar um processo? (Minutos)"));

def analisar_tempo (tempo):
    tempo_total = (8 * 60) / tempo
    return int(tempo_total);

print(analisar_tempo(tempo));