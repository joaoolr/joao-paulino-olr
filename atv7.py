lado1 = int(input("Primeiro lado ? "))
lado2 = int(input("Segundo  lado ? "))
lado3 = int(input("Terceiro lado ? "))

if lado1 == lado2 == lado3:
    print("equilatero")

elif lado1 != lado2 != lado3:
    print("escaleno")
else:
    print("isóceles")
