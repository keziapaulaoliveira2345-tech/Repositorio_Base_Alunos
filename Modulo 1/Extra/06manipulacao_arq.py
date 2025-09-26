# ler o arquivo e exibir o texto em letras maiusculas

with open("mensagem.txt", "r") as arquivo:
    for linha in arquivo: # aqui percorremos as linhas do arquivo
        print(linha.strip().upper()) # imprimimos cada linha em letra maisculas
# tiramos os espaços