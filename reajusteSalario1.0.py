reajuste = 0
percentual = 0

salario = float(input("Digite o salario: "))

if salario <= 280:
    reajuste = salario * 0.20
    percentual = 20
elif salario <= 700 and salario > 280:
    reajuste = salario * 0.15
    percentual = 15
elif salario <= 1500 and salario > 700:
    reajuste = salario * 0.10
    percentual = 10
else:
    reajuste = salario * 0.05
    percentual = 5

salarioReajustado = salario + reajuste

print(f"Salário antes do reajuste: R${salario}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R${reajuste}")
print(f"Novo salário: R${salarioReajustado}")
