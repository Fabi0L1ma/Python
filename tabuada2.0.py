# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
# não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
# conforme exemplo abaixo:

calculo = 0

tabuda = int(input("Montar a tabuada de: "))
valorInicial = int(input("Começar por: "))
valorFinal = int(input("Terminar em: "))

if valorInicial <= valorFinal:
    print(f"Vou montar a tabuada de {tabuda} começando em {valorInicial} e terminando em {valorFinal}:")
    for valorInicial in range(valorInicial, valorFinal + 1):
        calculo = tabuda * valorInicial

        print(f"{tabuda} x {valorInicial} = {calculo}")

else:
    print("VALORES INVALIDOS!")

