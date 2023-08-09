# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
# votar e ao final mostrar o número de votos de cada candidato.

qtd_joao = 0
qtd_maria = 0
qtd_carlos = 0

numeroEleitores = int(input("Digite o numero de eleitores: "))

for i in range(numeroEleitores):
    print("[11] - MARIA")
    print("[16] - JOÃO")
    print("[23] - CARLOS")
    voto = int(input("Digite o seu voto: "))

    if voto == 16:
        qtd_joao += 1
        print("VOTOU EM JOÃO!\n")
    elif voto == 11:
        qtd_maria += 1
        print("VOTOU EM MARIA!\n")
    elif voto == 23:
        qtd_carlos += 1
        print("VOTOU EM CARLOS!\n")
    else:
        print("VOTO NULO!\n")

print(f"QTD de votos do candidato João: {qtd_joao}")
print(f"QTD de votos da candidata Maria: {qtd_maria}")
print(f"QTD de votos do candidato Carlos: {qtd_carlos}")
