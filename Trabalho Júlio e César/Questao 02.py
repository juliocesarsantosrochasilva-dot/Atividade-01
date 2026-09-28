Usuario = "adimin"
Senha = 123
login = 0

while login == 0:
    print("==== MENU DE LOGIN ====")

    usuario_digitado = input("Digite seu nome de usuário: ")
    senha_digitada = int(input("Digite sua senha: "))

    if usuario_digitado == Usuario and senha_digitada == Senha:
        print("Login feito com sucesso!")
        login = 1
    else:
        print("Falha no login!")

while login == 1:
    print("\n==== MENU PRINCIPAL ====")
    print("1 - Logout")
    print("2 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        login = 0
        print("Voltando para o login...")

    elif opcao == 2:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
