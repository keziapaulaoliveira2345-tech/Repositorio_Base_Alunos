# ler e imprimir o conteudo do arquivo mensagem.txt

with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read()) # aqui estamos imprimindo o que o arquivo leu
# e neste caso, nao estamos armazenando em nenhuma variavel 