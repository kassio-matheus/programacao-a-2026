import subprocess

def mostrar_arquivos(diretorio):
    arquivos = subprocess.run(["ls", "-p"], capture_output=True, text=True, cwd=f"/Users{diretorio}").stdout.split("\n")
    return list(filter(None, arquivos))

def verificar_tipo(nome):
    if nome.endswith("/"):
        return "Pasta"
    return "Arquivo"

def abrir_arquivo (diretorio):
    subprocess.run(["open", diretorio], capture_output=False, text=False)
    return None

def procurar_arquivo(arquivos, diretorio, nome):
    if arquivos == []:
        return None
    
    for i in arquivos:
        print(i)
        
        if verificar_tipo(i) == "Pasta":
            if i[:-1] == nome:
                abrir_arquivo(f"/Users{diretorio}/{i[:-1]}")
                return f"/Users{diretorio}/{i[:-1]}"
            
            resultado = procurar_arquivo(
                mostrar_arquivos(f"{diretorio}/{i[:-1]}"),
                diretorio=f"{diretorio}/{i[:-1]}",
                nome=nome
            )

            if resultado:
                return resultado
        elif i == nome:
            abrir_arquivo(f"/Users{diretorio}/{nome}")
            return f"/Users{diretorio}/{i}"

nome_arquivo = input("Qual o nome do arquivo que deseja procurar?")
print(procurar_arquivo(mostrar_arquivos(""), diretorio="", nome=nome_arquivo))