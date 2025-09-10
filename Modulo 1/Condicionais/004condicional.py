# Crie um codigo em python que peça um numero ao usuario
# e exiba "Numero par" se ele for divisivel por 2.

# Etapas de resoluçao:

# 1) solicitar um numero ao usuario
# 2) verificar se o numero e par ou impar
# 3) informar se o numero e par ou impar

numero = float(input("Digite um numero: "))

if numero % 2 == 0:
    print(f' o numero {numero} e par. ')
else: 
    print(f' o numero {numero} e impar. ')