# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
# o número de alunos com média maior ou igual a 7.0.

alunos = [[],[]]
notas = [[0,0,0,0],[0,0,0,0]]
media = [[],[]]
somaNotas = 0

for i in range(2):
    somaNotas = 0
    alunos[i] = str(input("ALUNO: "))
    for j in range(4):
        notas[i][j] = float(input("NOTAS: "))
        somaNotas += notas[i][j]
    
    media[i] = somaNotas/4
        
    print("\n")
        
for i in range(2):
    print(f"ALUNO: {alunos[i]}")
    for j in range(4):
        print(f"NOTA: {notas[i][j]}")
    
    print(f"MEDIA: {media[i]}")
    print("\n")
    