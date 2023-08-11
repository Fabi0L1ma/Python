# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
# aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

# a. Maior e Menor Acerto;
# b. Total de Alunos que utilizaram o sistema;
# c. A Média das Notas da Turma.

acertos = 0
maiorAcerto = 0
menorAcerto = 999
qtdAluno = 0
medNotas = 0
somaNotas = 0

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
questao = []

print("RESPOSTA PODEM SER: [A], [B], [C], [D] e [E]")
while True:
    questao.clear()
    acertos = 0
    qtdAluno += 1
    for i in range(0, 10):
        questao.append(str(input(f"QUESTAO {i + 1}: ")))
        if questao[i] == gabarito[i]:
            acertos += 1
            
    somaNotas += acertos
        
    if acertos > maiorAcerto:
        maiorAcerto = acertos
    
    if acertos < menorAcerto:
        menorAcerto = acertos
    
    op = str(input("QUER CONTIUNUAR [S] ou [N]: "))
    if op == 'S':
        print("\n")
        continue
    else:
        print("\n")
        break

medNotas = somaNotas/qtdAluno

print(f"MAIOR ACERTO: {maiorAcerto}")
print(f"MENOR ACERTO: {menorAcerto}")
print(f"TOTAL DE ALUNOS QUE UTILIZARAM O SISTEMA: {qtdAluno}")
print(f"MEDIA DAS NOTAS DA TURMA: {round(medNotas, 2)}")