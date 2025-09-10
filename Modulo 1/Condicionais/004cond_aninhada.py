5#  tipo de triangulo
# crie um programa que receba três lados de um triangulo 
# verifique se os dois lados realmente podem formar um triangulo 
# e determine os triangulos em: 
# equilatero (todos os lados são iguais) 
# Isósceles (dois lados iguais) 
# escaleno (todos os lados diferentes)


a= int(input("Digite o valor do lado a: "))
b= int(input("Digite o valor do lado b: "))
c= int(input("Digite o valor do lado c: "))

# verificar se os lados formam um triangulo:
if a +b > c and a+c > b and b+c > a: # condiçao para formaçao do triangulo
    if a == b:
        if b == c: 
            print(f' os lados do triangulo sao {a}, {b} e {c}: Triangulo equilatero')
        else:
            print(f" os lados do triangulo sao {a}, {b} e {c}: Triangulo isosceles.")
    else: # nao e possivel formar um triangulo
        if b == c or a == c:
            print(f" os lados do triangulo sao {a}, e {b} e {c}: Triangulo isosceles.")
        else:
            print(f" os lados do triangulo sao {a}, {b} e {c}: triangulo escaleno.")
else: 
    print("os lados nao formam um triangulo valido.")
