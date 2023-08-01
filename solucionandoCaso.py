# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
# como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

qtdResp = 0

print("\nResponder: [SIM] ou [NAO] \n")
resp1 = str(input("Telefonou para vítima? "))

if resp1 == 'SIM':
    qtdResp += 1
else:
    qtdResp += 0

resp2 = str(input("Esteve no local do crime? "))

if resp2 == 'SIM':
    qtdResp += 1
else:
    qtdResp += 0

resp3 = str(input("Mora perto da vítima? "))

if resp3 == 'SIM':
    qtdResp += 1
else:
    qtdResp += 0

resp4 = str(input("Devia para a vítima? "))

if resp4 == 'SIM':
    qtdResp += 1
else:
    qtdResp += 0

resp5 = str(input("Já trabalhou com a vítima? "))

if resp5 == 'SIM':
    qtdResp += 1
else:
    qtdResp += 0

if qtdResp == 2:
    print("SUSPEITA!")
elif qtdResp == 3 or qtdResp == 4:
    print("CÚMPLICE!")
elif qtdResp == 5:
    print("ASSASSINO!")
else:
    print("INOCENTE!")