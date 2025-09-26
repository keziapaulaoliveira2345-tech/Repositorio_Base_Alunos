# Criar arquvios, recebendo informaçao do usuario

# solicitaçao de entrada
nome= input("Digite seu nome completo: ")
email= input("Digite seu email: ")


# criar arquvio 
arquivo= open("pessoa.txt", "a",encoding="utf-8") # estamos criando o arquivo  e
# armazena na variavel arquivo, o modo "a" escreve sempre no final,
# enconding utf-8 é para utilizar o conjunto de caracteres que engloba
# a linha portuguesa
arquivo.write(nome +'|'+ email + '\n') # .white é para escrever e o 
# \n é para pular a linha
arquivo.close() # .close é para fechar o arquivo.