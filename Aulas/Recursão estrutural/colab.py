def procurarArquivo(arquivos, nome, diretorio):
    for arquivo in arquivos:
        if isinstance(arquivo, tuple):
            resultado = procurarArquivo(arquivo[1], nome, diretorio=f"{diretorio}/{arquivo[0]}")
            if resultado:
                return resultado

        elif isinstance(arquivo, list):
            resultado = procurarArquivo(arquivo, nome, diretorio)
            if resultado:
                return resultado

        elif arquivo == nome:
            return f"{diretorio}/{arquivo}"

arquivos = (
    "main", [ "a1.py",
              "a2.py",
              ("semana1", [ "a1.py",
                            "a2.py",
                            "a3.txt",
                            "b1.py"
            ]
              ),
    ("semana2", [ "c1.txt",
                         ("segunda", [ "c.txt",
                                       "a.txt"
                                     ]
                         ),
                         ("terca",  [ "a.txt",
                                      "b.txt",
                                      "c.txt"
                                     ]
                         )
                       ]
           )
         ]
)

print(procurarArquivo(arquivos, nome="c1.txt", diretorio="/main"))