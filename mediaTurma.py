# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

somaQtdAlunos = 0
mediaAlunos = 0

qtdTurma = int(input("Digite a QTD de turmas: "))

for i in range(qtdTurma):
    qtdAlunos = int(input("Digite a QTD de alunos [ATÉ 40 PESSOAS]: "))

    if qtdAlunos <= 40 and qtdAlunos >= 0:
        somaQtdAlunos += qtdAlunos
    else:
        print("QTD de alunos invalida!\n")
        while True:
            qtdAlunos = int(input("QTD de alunos [ATÉ 40 PESSOAS]: "))

            if qtdAlunos <= 40 and qtdAlunos >= 0:
                break
            else:
                continue

mediaAlunos = somaQtdAlunos/qtdTurma

print(f"Média de alunos por turma: {mediaAlunos}")