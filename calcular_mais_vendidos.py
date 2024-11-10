produto = [ {"nome_do_produto":"", "quantidade": 0}, {"nome_do_produto": "", "quantidade": 0}]

print("Calcular qual produto foi mais vendido no supermercado\n")

def obter_dados():
    produto1 = input("Qual o nome do primeiro produto? ")
    quant_produto1 = int(input(f"Qual a quantidade vendida do {produto1}? \n"))
    produto2 = input("Qual o nome do segundo produto? ")
    quant_produto2 = int(input(f"Qual a quantidade vendida do {produto2}? \n"))
    return produto1, quant_produto1, produto2, quant_produto2
produto1, quant_produto1, produto2, quant_produto2 = obter_dados()

def dados():
    produto[0]["nome_do_produto"] = produto1
    produto[0]["quantidade"] = quant_produto1
    produto[1]["nome_do_produto"] = produto2
    produto[1]["quantidade"] = quant_produto2
    return produto[0], produto[1]
produto[0], produto[1] = dados()

if quant_produto1 > quant_produto2:
    print(f"O produto com maior venda foi {produto1}")
elif quant_produto1 == quant_produto2:
    print("A quantidade de produtos vendidos foram as mesmas")
else: 
    print(f"O produto mais vendido foi {produto2}")
