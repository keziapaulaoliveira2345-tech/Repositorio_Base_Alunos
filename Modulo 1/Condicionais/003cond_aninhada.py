# 3. Classificaçao por idade
# faça um programa que leia a idade de uma pessoa e classifique-a em:
# criança : menor que 12 anos
# adolescente: entre 12 a 17 anos
# adulto: maior ou igual a 18 anos
# utilize a estrutura de condicional aninhada

idade= int(input("qual e a sua idade:"))

if idade > 0:
    if idade >= 18:
        print (f" Voce tem {idade} anos e e um adulto. ")
    elif 12 <= idade <= 17:
        print (f" Voce tem {idade} e e adolescente. ")
    else: 
        print(f"Voce tem {idade} e e uma criança")
else: 
    print("idade nao pode ser negativa, digite uma idade valida")

