conta = input("crie um email:")
senha = int(input("crie uma senha:"))

login = input("digite se email:")
loginSenha = int(input("digite sua senha"))

if conta == login and senha == loginSenha:
    print("usuário logado")

elif conta != login and senha != loginSenha:
    print("ambos estão incorretos")

elif conta != login:
    print("email incorreto")

elif senha != loginSenha:
    print("senha incorreta")
