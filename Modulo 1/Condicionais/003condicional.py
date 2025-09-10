# Criar um codigo python que indique se a temperaturaesta agradavel ou nao
# Condiçoes: 
# Temperatura >= 30°informar que esta muito quente
# Temperatura>= 20° informar que a temperatura esta agradavel 
# Temperatura >= 10° informar que esta frio
# TEmperatura abaixo de 10° informar que esta muito frio 

# Etapas para resoluçao:
# 1) Solicitar a temperatura para o usuario
# 2) verificar a condicional
# 3) imprimir a resposta segundo a temperatura

temperatura =float(input("Digite a temperatura do dia: "))

# if condiçao: 
   # bloco de codigo a ser executado
# elif condiçao: 
   # bloco de codigo a ser executado 
# else: 
   # bloco de codigo a ser executado

if temperatura >= 30:
     print(f"a temperatura do dia e {temperatura}°C e o dia esta muito quente.")
elif temperatura >= 20:
      print(f" a temperatura do dia e {temperatura}°C e o dia esta agradavel.")
elif temperatura >= 10:
     print(f" a temperatura do dia e {temperatura}°C e o dia esta frio.")
else:
     print(f" a temperatura do dia e {temperatura}°C e o dia esta muito frio.")

