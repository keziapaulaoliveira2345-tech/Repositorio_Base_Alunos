# solicitamos dois numeros ao usuario sem informar o tipo de dado 

num1= input("Digite o primeiro numero:")
num2= input("Digite o segundo numero:")


try:
    num1=int(num1)
    num2=int(num2)

    print(f" soma dos numeros é {num1 + num2}")
except:
    print("Digite um numero correto.")