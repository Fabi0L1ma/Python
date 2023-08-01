# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
# informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

resp = 0

num = int(input("Número da tabuada: "))

for i in range(1, 11):
    resp = num * i
    print(f"{num} x {i} = {resp}")