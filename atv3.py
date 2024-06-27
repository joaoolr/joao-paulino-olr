nota1 = float(input("qual é a primeira nota?"))
nota2 = float(input("qual é a segunda nota?"))
nota3 = float(input("qual é a terceira nota?"))
nota4 = float(input("qual é a quarta nota?"))

media = ((nota1 + nota2 + nota3 + nota4) / 4)

if media < 50:
    print("reprovado")
elif media >= 50 and media <= 69:
    print("recuperaçao")
elif media >= 70:
    print("aprovado")