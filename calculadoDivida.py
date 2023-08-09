# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
# dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo

valorTotalDivida = 0
valorJuros = 0
valorParcela = 0

divida = float(input("VALOR DA DIVIDA: R$"))

while True:
    print("CALCULADORA DE DIVIDA: ")
    for i in range(0, 13, 3):
        if i == 0:
            i = 1
            print(i)
        else:
            print(i)
    qtdParcelas = int(input("QTD DE PARCELAS: "))

    if qtdParcelas == 1 or qtdParcelas == 3 or qtdParcelas == 6 or qtdParcelas == 9 or qtdParcelas == 12:
        break
    else:
        print("VALOR INVALIDO!\n")
        continue

while True:
    for j in range(0, 26, 5):
        if j == 5:
            j = 10
            print(j)
        elif j != 10:
            print(j)
    opJuros = int(input("% JUROS: "))

    if opJuros == 0:
        valorJuros = divida * opJuros
        valorTotalDivida = divida + valorJuros
        valorParcela = valorTotalDivida/qtdParcelas

        print(f"VALOR DA DIVIDA: R${round(valorTotalDivida, 2)}   VALOR DOS JUROS: R${round(valorJuros, 2)}   QTD PARCELAS: {qtdParcelas}    VALOR DE PARCELAS: R${round(valorParcela, 2)}")
        break

    elif opJuros == 10:
        opJuros = opJuros/100
        valorJuros = divida * opJuros
        valorTotalDivida = divida + valorJuros
        valorParcela = valorTotalDivida/qtdParcelas

        print(f"VALOR DA DIVIDA: R${round(valorTotalDivida, 2)}   VALOR DOS JUROS: R${round(valorJuros, 2)}   QTD PARCELAS: {qtdParcelas}    VALOR DE PARCELAS: R${round(valorParcela, 2)}")
        break

    elif opJuros == 15:
        opJuros = opJuros/100
        valorJuros = divida * opJuros
        valorTotalDivida = divida + valorJuros
        valorParcela = valorTotalDivida/qtdParcelas

        print(f"VALOR DA DIVIDA: R${round(valorTotalDivida, 2)}   VALOR DOS JUROS: R${round(valorJuros, 2)}   QTD PARCELAS: {qtdParcelas}    VALOR DE PARCELAS: R${round(valorParcela, 2)}")
        break

    elif opJuros == 20:
        opJuros = opJuros/100
        valorJuros = divida * opJuros
        valorTotalDivida = divida + valorJuros
        valorParcela = valorTotalDivida/qtdParcelas

        print(f"VALOR DA DIVIDA: R${round(valorTotalDivida, 2)}   VALOR DOS JUROS: R${round(valorJuros, 2)}   QTD PARCELAS: {qtdParcelas}    VALOR DE PARCELAS: R${round(valorParcela, 2)}")
        break

    elif opJuros == 25:
        opJuros = opJuros/100
        valorJuros = divida * opJuros
        valorTotalDivida = divida + valorJuros
        valorParcela = valorTotalDivida/qtdParcelas

        print(f"VALOR DA DIVIDA: R${round(valorTotalDivida, 2)}   VALOR DOS JUROS: R${round(valorJuros, 2)}   QTD PARCELAS: {qtdParcelas}    VALOR DE PARCELAS: R${round(valorParcela, 2)}")
        break

    else:
        print("VALOR INVALIDO!\n")
        continue