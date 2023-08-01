valor_hora = float(input("Valor hora: R$"))
horas_mes = int(input("Horas trabalhadas no mês: "))


salario_bruto = valor_hora * horas_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"Salario bruto: R${salario_bruto}")
print(f"IR: R${ir}")
print(f"INSS: R${inss}")
print(f"Sindicado: R${sindicato}")
print(f"Salario liquido: R${salario_liquido}")



