# cadastrar de produtos com relatorio 
# crie um programa em python que permita cadastrar produtos
# salvar essas informaçoes em um arquivo chamado prodtudos,txt
# o programa deve permitir:
# 1) inserir o nome do produto de preço 
# 2) gravar os produtos no arquivo (um por linha)
# 3) ler os dados do arquivo e gerar um relatorio com:
# - lista de produtod cadastrados 
# -media dos prços 
# - o produto mais caro e o mais barato 

# criar o arquivo produtos.txt e escrever os produtos 
with open ("produtos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Cafe, 36.00\n")
    arquivo.write("chá,10.00\n")
    arquivo.write("suco,18.50\n")
    arquivo.write("refrigerante,17.50\n")
    arquivo.write("agua, 5.50\n")

# ler os produtos do arquivo
produtos=[]
with open("produtos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome, preco= linha.strip().split(",")
        produtos.append((nome, float (preco))) 


# calcular a media do mais cara e o mais barato
total= 0
mais_caro= produtos[0]
mais_barato= produtos [0]

for nome, preco in produtos : 
    total+=preco # percore a lista produtos e soma cada preço encontrado
    if preco > mais_caro[1]:
        mais_caro= (nome, preco)

    if preco < mais_barato[1]:
        mais_barato= (nome, preco)

media= total/len(produtos)

# criar o relatorio 
with  open("Relatorio_produtos.txt", "w", encoding="utf-8") as relatorio:
    relatorio.write("lista de produtos\n")
    for nome, preco in produtos:
        relatorio.write(f"{nome}: R$ {preco:.2f}\n")

    relatorio.write(f"\npreço medio: R$ {mais_barato}\n")
    relatorio.write(f" produto mais caro: {mais_caro[0]} R${mais_caro[1]:.2f}\n")
    relatorio.write(f" produto mais barato: {mais_caro[0]} R${mais_caro[1]:.2f}\n")
