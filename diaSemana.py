#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
#outro valor deve aparecer valor inválido.

print("[1] - DOMINGO")
print("[2] - SEGUNDA-FEIRA")
print("[3] - TERÇA-FEIRA")
print("[4] - QUARTA-FEIRA")
print("[5] - QUINTA-FEIRA")
print("[6] - SEXTA-FEIRA")
print("[7] - SABADO")
op = int(input("Opção: "))

if op == 1:
    print("O dia escolhido foi DOMINGO")
elif op == 2:
    print("O dia escolhido foi SEGUNDA-FEIRA")
elif op == 3:
    print("O dia escolhido foi TERÇA-FEIRA")
elif op == 4:
    print("O dia escolhido foi QUARTA-FEIRA")
elif op == 5:
    print("O dia escolhido foi QUINTA-FEIRA")
elif op == 6:
    print("O dia escolhido foi SEXTA-FEIRA")
elif op == 7:
    print("O dia escolhido foi SABADO")
else:
    print("Dia INVALIDO!")