# 2. Paridade e tamanho do numero
# Crie um codigo que receba um numero inteiro e informa:
# - se e par ou inpar
# - e, ao mesmo tempo, se e maior que 10 ou menor ou igual a 10
# utilize condicionais aninhadas para organizar as verificaçoes

num= int (input("Digite um numero inteiro: "))
if num % 2 == 0: 
    if num > 10: # e maior que 10?
      print("o numero digitado e par e maior que 10.") 
      
    
      print("o numero digitado e par e menor a 10.")
    if num <10:
       print("o numero digitado e impar e maior que 10.")
    else:
       print(" o numero digitado e menor que 10.")