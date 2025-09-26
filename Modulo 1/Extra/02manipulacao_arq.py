# ler um arquivo 

arquivo= open("pessoa.txt", "r") # a leitura esta sendo feita na memoria
conteudo= arquivo.read() # eu armazeno a leitura em uma variavel 
print(conteudo) # peço para imprimir a leitura
arquivo.close() # sempre que utilizamos  a funcao open() precisamos finalizar
# fechando o arquivo 