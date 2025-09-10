#CRie um codigo que receba 3 notas, e calcule a media
# e informe se o aluno esta aprovado, em recuperaçao
# ou reprovado

#OBS: aprovado media >= 7
# recuperaçao media > 4
# Reprovado media <$

# etapas
#1) Solicitar as notas ao usuario 
n1 = float(input("DIgite a primeira nota:"))
n2= float(input("Digite a segunda nota: "))
n3= float(input("Digite a terceira nota: "))

#2) calcular a media
media= (n1 + n2 + n3) /3

#3) chegar a condiçao do aluno
if media >=7:
   print(f"O aluno tem media {media:} e esta aprovado.")
elif 5 <= media < 7 : # o mesmo que => elif media >= 5 and media < 7:
    print(f" o aluno teve media {media:.2f} e esta em recuperaçao")
else: 
    print (f"o aluno teve media {media:2.f} e esta reprovado. ")

#4) informar o resultado.