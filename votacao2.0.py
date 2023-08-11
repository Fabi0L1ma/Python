# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
# utilizados são:

# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos 
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero

qtdVoto1 = 0
qtdVoto2 = 0
qtdVoto3 = 0
qtdVoto4 = 0
qtdNulo = 0
qtdBranco = 0
totalVotos = 0
porcentagemNulo = 0
porcentagemBranco = 0

while True:
    print("VOTACAO:")
    print("[1] - JOSE")
    print("[2] - JOAO")
    print("[3] - MARIA")
    print("[4] - ELENA")
    print("[5] - VOTO NULO")
    print("[6] - VOTO EM BRANCO")
    print("[0] - SAIR")
    voto = int(input("DIGITE O SEU VOTO: "))
    
    if voto == 1:
        print("VOCE VOTOU NO JOSE!\n")
        qtdVoto1 += 1
    
    elif voto == 2:
        print("VOCE VOTOU NO JOAO!\n")
        qtdVoto2 += 1
        
    elif voto == 3:
        print("VOCE VOTOU NA MARIA!\n")
        qtdVoto3 += 1
    
    elif voto == 4:
        print("VOCE VOTOU NA ELENA!\n")
        qtdVoto4 += 1
        
    elif voto == 5:
        print("VOTOU NULO!\n")
        qtdNulo += 1
        
    elif voto == 6:
        print("VOTOU EM BRANCO!\n")
        qtdBranco += 1
        
    elif voto == 0:
        break
    else:
        print("VALOR INDISPONIVEL!\n")
        continue
    
    totalVotos  = qtdVoto1 + qtdVoto2 + qtdVoto3 + qtdVoto4 + qtdNulo + qtdBranco
    
    porcentagemNulo = (qtdNulo * 100)/totalVotos
    porcentagemBranco = (qtdBranco * 100)/totalVotos
    
print(f"\nQTD DE VOTOS JOSE: {qtdVoto1}")
print(f"QTD DE VOTOS JOAO: {qtdVoto2}")
print(f"QTD DE VOTOS MARIA: {qtdVoto3}")
print(f"QTD DE VOTOS ELENA: {qtdVoto4}")
print(f"QTD DE VOTOS NULOS: {qtdNulo}           PORCENTAGEM: {round(porcentagemNulo, 2)}%")
print(f"QTD DE VOTOS EM BRANCO: {qtdBranco}       PORCENTAGEM: {round(porcentagemBranco, 2)}%")
        