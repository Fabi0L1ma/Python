# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser
# pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido
# deve ser encerrado.

valorUnitario = 0
valorTotal = 0
produtos = []
vaolresPorProdutos = []
qtdPorProduto = []
cont = 0

while True:
    cont += 1
    print("ESPECIFICACAO     CODIGO   PRECO")
    print("CACHORRO QUENTE   100      R$1.20")
    print("BAURU SIMPLES     101      R$1.30")
    print("BAURU COM OVO     102      R$1.50")
    print("HAMBURGUER        103      R$1.20")
    print("CHEESEBURGUER     104      R$1.30")
    print("REFRIGERANTE      105      R$1.00")
    op = int(input("Digite a opcao: "))

    if op == 100:
        valorProduto = 1.20
        qtd = int(input("QTD: "))
        valorUnitario = valorProduto * qtd
        qtdPorProduto.append(qtd)
        produtos.append("CACHORRO QUENTE")
        vaolresPorProdutos.append(valorUnitario)

    elif op == 101:
        valorProduto = 1.30
        qtd = int(input("QTD: "))
        valorUnitario = valorProduto * qtd
        qtdPorProduto.append(qtd)
        produtos.append("BAURU SIMPLES  ")
        vaolresPorProdutos.append(valorUnitario)
    
    elif op == 102:
        valorProduto = 1.50
        qtd = int(input("QTD: "))
        valorUnitario = valorProduto * qtd
        qtdPorProduto.append(qtd)
        produtos.append("BAURU COM OVO  ")
        vaolresPorProdutos.append(valorUnitario)

    elif op == 103:
        valorProduto = 1.20
        qtd = int(input("QTD: "))
        valorUnitario = valorProduto * qtd
        qtdPorProduto.append(qtd)
        produtos.append("HAMBURGUER     ")
        vaolresPorProdutos.append(valorUnitario)
    
    elif op == 104:
        valorProduto = 1.30
        qtd = int(input("QTD: "))
        valorUnitario = valorProduto * qtd
        qtdPorProduto.append(qtd)
        produtos.append("CHEESEBURGUER  ")
        vaolresPorProdutos.append(valorUnitario)

    elif op == 105:
        valorProduto = 1.00
        qtd = int(input("QTD: "))
        valorUnitario = valorProduto * qtd
        qtdPorProduto.append(qtd)
        produtos.append("REFRIGERANTE  ")
        vaolresPorProdutos.append(valorUnitario)

    else:
        print("CODIGO INVALIDO!\n")
        continue

    valorTotal += valorUnitario

    continuarCompra = str(input("DESEJA CONTINUAR [S] ou [N]: "))
    print("\n")

    if continuarCompra == 'S':
        continue
    else:
        break


print("PRODUTO                 QTD         VALORES UNITARIOS\n")
for i in range(len(produtos)):
    print(f"{produtos[i]}         {qtdPorProduto[i]}           R${vaolresPorProdutos[i]}")

    if i != i:
        print("\n")

print(f"\nTotal a ser pago: R${valorTotal}")