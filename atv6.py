n1 = float(input("qual é o primeiro numero?:"))
n2 = float(input("qual é o segundo numero?:"))
n3 = float(input("qual é o terceiro numero?:"))

if n1 > n2 and n1 > n3:
    print(f"O Primerio numero({(n1)}) é maior")
    if n2 == n3:
        print(f"O Segundo numero({(n2)}) e o Terceiro numero ({(n3)}) sao iguais")

if n2 > n1 and n2 > n3:
    print(f"O Segundo numero({(n2)}) é maior")
    if n1 == n3:
        print(f"O Primeiro numero({(n1)}) e o Terceiro numero ({(n3)}) sao iguais")

if n3 > n1 and n3 > n2:
    print(f"O Terceiro numero({(n3)}) é maior")
    if n1 == n3:
        print(f"O Primeiro numero({(n1)}) e o Segundo numero ({(n2)}) sao iguais")

if n1 == n2 == n3:
    print("Os tres numero sao iguais")