quantidade_linhas = int(input())

for i in range(1, quantidade_linhas + 1):
    linhas = ("-" + str(i)) * (i - 1)
    print(i, linhas, sep="")