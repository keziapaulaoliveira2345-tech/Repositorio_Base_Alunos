# CRie um codigo python que verifique se a senha digitada
# pelo usuario for "1234", exiba "Acesso permitido".

# etapas para resoluçao 
#  criar uma variavel e a atribuir a ela uma senha
# Atraves de um input solicitar a senha ao usuario
# atraves da condicional checar se a senha e igual a senha armazenada
# liberar ou nao o acesso ao usuario

senha_paula= "2804"

senha= input("Digite sua senha: ")

if senha == senha_paula:
    print("Acesso liberado.")

else: 
    print("Acesso negado. Tente novamente")

