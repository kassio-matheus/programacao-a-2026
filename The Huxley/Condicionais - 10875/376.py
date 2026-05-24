quantidade_livros = int(input());
quantidade_alunos = int(input());

livros_por_alunos = quantidade_alunos / quantidade_livros;

if(livros_por_alunos <= 8):
    print("A")
elif(livros_por_alunos <= 12):
    print("B")
elif(livros_por_alunos <= 18):
    print("C")
else:
    print("D")