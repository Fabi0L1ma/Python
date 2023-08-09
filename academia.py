# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
# magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
# seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
# programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
# magro, além da média das alturas e dos pesos dos clientes

codigo = []
altura = []
peso = []
maiorAltura, menorAltura, maiorPeso, menorPeso = 0, 9999, 0, 9999
posMaisAlto, posMaisBaixo, posMaiorPeso, posMenorPeso = 0, 0, 0, 0
somaAltura, mediaAltura = 0, 0
somaPeso, mediaPeso = 0, 0

i = 0

while True:
    codigo.append(str(input("Codigo: ")))

    if codigo[i] != '0':
        altura.append(float(input("Altura: ")))
        peso.append(float(input("Peso: ")))

        if altura[i] > maiorAltura:
            maiorAltura = altura[i]
            posMaisAlto = i

        if altura[i] < menorAltura:
            menorAltura = altura[i]
            posMaisBaixo = i

        if peso[i] > maiorPeso:
            maiorPeso = peso[i]
            posMaiorPeso = i

        if peso[i] < menorPeso:
            menorPeso = peso[i]
            posMenorPeso = i

        somaAltura += altura[i]
        somaPeso += peso[i]

        i += 1

    else:
        print("\n")
        break

codigo.pop()

mediaAltura = somaAltura/i
mediaPeso = somaPeso/i

for i in range(len(codigo)):
    if posMaisAlto == i:
        print("MAIS ALTO: ")
        print(f"CODIGO: {codigo[i]}")
        print(f"ALTURA: {round(altura[i], 3)}\n")

    if posMaisBaixo == i:
        print("MAIS BAIXO: ")
        print(f"CODIGO: {codigo[i]}")
        print(f"ALTURA: {round(altura[i], 3)}\n")

    if posMaiorPeso == i:
        print("MAIOR PESO: ")
        print(f"CODIGO: {codigo[i]}")
        print(f"PESO: {round(peso[i], 3)}\n")

    if posMenorPeso == i:
        print("MENOR PESO: ")
        print(f"CODIGO: {codigo[i]}")
        print(f"PESO: {round(peso[i], 3)}\n")

print(f"MEDIA DE ALTURA: {round(mediaAltura)}")
print(f"MEDIA DE PESO: {round(mediaPeso)}")
