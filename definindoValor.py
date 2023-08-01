# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
# operação deve ser acompanhado de uma frase que diga se o número é:

# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal

calculo = 0

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("[1] - ADIÇÃO ")
print("[2] - SUBTRAÇÃO")
print("[3] - MULTIPLICACAO")
print("[4] - DIVISÃO")
op = int(input("OPÇÃO: "))

if op == 1:
    print("SOMA: ")
    calculo = num1 + num2
    print(f"RESULTADO = {calculo}")

elif op == 2:
    print("SUBTRAÇÃO: ")
    calculo = num1 - num2
    print(f"RESULTADO: {calculo}")

elif op == 3:
    print("MULTIPLICAÇÃO: ")
    calculo = num1 * num2
    print(f"RESULTADO = {calculo}")

elif op == 4:
    print("DIVISÃO: ")
    calculo = num1/num2
    print(f"RESULTADO = {calculo}")

else:
    print("OPÇÃO INVALIDA!")

if calculo % 2 == 0:
    print("O número é PAR!")
else:
    print("O número é IMPAR!")

if calculo >= 0:
    print("O número é POSITIVO!")
else:
    print("O número é NEGATIVO!")

if type(calculo) == int:
    print("O número é INTEIRO")
else:
    print("O número é DECIMAL")