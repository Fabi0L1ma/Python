lado1 = float(input("Primeira medida: "))
lado2 = float(input("Segunda medida: "))
lado3 = float(input("Terceira medida: "))

if lado1 == lado2 and lado1 == lado3:
    print("TRIÂNGULO EQUILÁTERO")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("TRIÂMGULO ISÓSCELES")
else:
    print("TRIÂNGULO ESCALENO")