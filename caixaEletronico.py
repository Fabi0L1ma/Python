# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
# de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na
# máquina.
# a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
# 5 e uma nota de 1;
# b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
# de 10, uma nota de 5 e quatro notas de 1

valorSaque = float(input("Digite o valor a ser sacado: R$"))

if valorSaque >= 10 and valorSaque <= 600:

    cem = int(valorSaque/100)
    valorSaque = valorSaque - (cem*100)

    cinquenta = int(valorSaque/50)
    valorSaque = valorSaque - (cinquenta*50)

    dez = int(valorSaque/10)
    valorSaque = valorSaque - (dez*10)

    cinco = int(valorSaque/5)
    valorSaque = valorSaque - (cinco*5)

    um = int(valorSaque)

    print("CEDULAS: ")
    print(f"R$100  QTD: {cem}")
    print(f"R$50   QTD: {cinquenta}")
    print(f"R$10   QTD: {dez}")
    print(f"R$5    QTD: {cinco}")
    print(f"R$1   QTD: {um}")

else:
    print("VALOR INDVALIDO!")