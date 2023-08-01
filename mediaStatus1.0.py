#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
#a sua média. A atribuição de conceitos obedece à tabela abaixo:

somaNotas = 0

for i in range(2):
    nota = float(input("Digite a nota: "))
    i += 1
    somaNotas += nota

media = somaNotas/2

if media >= 9 and media <= 10:
    print(f"MÉDIA: {media} CONCEITO: A (APROVADO)")
elif media < 9 and media >= 7.5:
    print(f"MÉDIA: {media} CONCEITO: B (APROVADO)")
elif media < 7.5 and media >= 6:
    print(f"MÉDIA: {media} CONCEITO: C (APROVADO)")
elif media < 6 and media >= 4:
    print(f"MÉDIA: {media} CONCEITO: D (REPROVADO)")
elif media < 4 and media >= 0:
    print(f"MÉDIA: {media} CONCEITO: E (REPROVADO)")
