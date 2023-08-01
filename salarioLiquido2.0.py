#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
#depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
#Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
#descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR:

#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%

valorHora = float(input("Valor hora: R$"))
qtdHoras = int(input("QTD de horas trabalhadas no mês: "))

salarioBruto = valorHora * qtdHoras

print(f"Salario bruto: R${salarioBruto}")

if salarioBruto <= 900:
    ir = salarioBruto * 0
    print("IR: ISENTO")
elif salarioBruto > 900 and salarioBruto <= 1500:
    ir = salarioBruto * 0.05
    print(f"IR (5%): R$ {ir})")
elif salarioBruto > 1500 and salarioBruto <= 2500:
    ir = salarioBruto * 0.10
    print(f"IR (10%): R$ {ir})")
else:
    ir = salarioBruto * 0.20
    print(f"IR (20%): R$ {ir})")

inss = salarioBruto * 0.10

print(f"INSS (10%): R${inss}")

fgts = salarioBruto * 0.11

print(f"FGTS (11%): R${fgts}")

totalDesconto = ir + inss

print(f"Total de desconto: R${totalDesconto}")

salarioLiquido = salarioBruto - totalDesconto

print(f"Salário liquido: R${salarioLiquido}")