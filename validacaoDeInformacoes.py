# Faça um programa que leia e valide as seguintes informações:

# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = str(input("Digite o seu nome [POSSUIR MAIS DE 3 CARACTERES]: "))

    tamnhoNome = len(nome)

    if tamnhoNome > 3:
        print("\n")
        break
    else:
        print("QTD DE CARACTERE INVALIDA!\n")
        continue

while True:
    idade = int(input("Digite a idade [ENTRE 0 À 150]: "))

    if idade >= 0 and idade <= 150:
        print("\n")
        break
    else:
        print("IDADE INVALIDA!\n")
        continue

while True:
    salario = float(input("Salario [TEM QUE SER MAIOR QUE 0]: R$"))

    if salario > 0:
        print("\n")
        break
    else:
        print("SALARIO INVALIDO!\n")
        continue

while True:
    sexo = str(input("Digite o sexo [M] ou [F]: "))

    if sexo == 'M' or sexo == 'F':
        print("\n")
        break
    else:
        print("SEXO INVALIDO!\n")
        continue

while True:
    estadoCivil = str(input("Digite o estado civil [S, C, V, D]: "))

    if estadoCivil == 'S' or estadoCivil == 'C' or estadoCivil == 'V' or estadoCivil == 'D':
        print("\n")
        break
    else:
        print("TIPO INVALIDO!\n")
        continue