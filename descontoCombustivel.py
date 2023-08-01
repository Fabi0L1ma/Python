# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro
# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

desconto = 0

print("Tipo de combustivel: ")
print("[A] - Álcool")
print("[G] - Gasolina")
tipoCombustivel = str(input("Opção: "))

if tipoCombustivel == 'A':
    qtdCombustivel = int(input("QTD de ALCOOL: "))
    valorCombustivel = qtdCombustivel * 1.90

    if qtdCombustivel <= 20 and qtdCombustivel > 0:
        valorCombustivel = valorCombustivel - (valorCombustivel * 0.03)
        print(f"Valor a ser pago com 3% de DESCONTO: R${round(valorCombustivel, 2)}")

    elif qtdCombustivel > 20:
        valorCombustivel = valorCombustivel - (valorCombustivel * 0.05)
        print(f"Valor a ser pago com 5% de DESCONTO: R${round(valorCombustivel, 2)}")

if tipoCombustivel == 'G':
    qtdCombustivel = int(input("QTD de GASOLINA: "))
    valorCombustivel = qtdCombustivel * 2.50

    if qtdCombustivel <= 20 and qtdCombustivel > 0:
        valorCombustivel = valorCombustivel - (valorCombustivel * 0.04)
        print(f"Valor a ser pago com 4% de DESCONTO: R${round(valorCombustivel , 2)}")

    elif qtdCombustivel > 20:
        valorCombustivel = valorCombustivel - (valorCombustivel * 0.06)
        print(f"Valor a ser pago com 6% de DESCONTO: R${round(valorCombustivel)}")
