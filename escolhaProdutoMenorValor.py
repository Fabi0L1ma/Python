menor = 9999

for i in range(3):
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    i += 1

    if preco < menor:
        menor = preco
        produtoEscolhido = produto

print(f"Produto que deve ser comprado é o {produtoEscolhido} que custa R${menor}")
