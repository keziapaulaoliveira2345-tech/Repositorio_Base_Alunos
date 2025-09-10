# 1) entrada de dados
num= int(input("Digite um numero inteiro: "))
# 2) Condicional para verificar se o numero e maior ou igual a zero
if num>=0:
   # condicional para chegar se o numero e zero 
   if num == 0:
    print ("O numero digitado e zero.") # informa que o numero e zero
   else: # informa que o numero e positivo
     print (f" o numero {num} e positivo. ")
# se o if for falso, entra no else e, informa que o numero e negativo