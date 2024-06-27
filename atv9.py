conta = input("crie um email:")
senha = (input("crie uma senha com 8 caracteres:"))

tamSenha = len(senha)

if tamSenha < 8:
    print("sua senh n possui o tamanho necessario")

else:
    print("tudo certo")