salario = float(input("Qual é o seu salario? R$"))

if salario <= 280:
    print("Salario antes:R$",salario)
    print("O salario aumentou em 20%")
    reajuste = salario * 1.20
    aumento = reajuste - salario
    print("O aumento salarial foi de R$",aumento)
    print("Seu novo salario é de R$",reajuste)
    
elif salario >= 281 and salario <=700:
    print("Salario antes:R$",salario)
    print("O salario aumentou em 15%")
    reajuste = salario * 1.15
    aumento = reajuste - salario
    print("O aumento salarial foi de R$",aumento)
    print("Seu novo salario é de R$",reajuste)

elif salario >= 701 and salario <=1500:
    print("Salario antes:R$",salario)
    print("O salario aumentou em 10%")
    reajuste = salario * 1.10
    aumento = reajuste - salario
    print("O aumento salarial foi de R$",aumento)
    print("Seu novo salario é de R$",reajuste)

elif salario >= 1501:
    print("Salario antes:R$",salario)
    print("O salario aumentou em 5%")
    reajuste = salario * 1.05
    aumento = reajuste - salario
    print("O aumento salarial foi de R$",aumento)
    print("Seu novo salario é de R$",reajuste)