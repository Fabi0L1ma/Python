numeros = []

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

numeros.append(n1)
numeros.append(n2)
numeros.append(n3)

numeros.sort()

maior = numeros[2]
menor = numeros[0]

print(f"Maior: {maior}")
print(f"Menor: {menor}")