usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")

cont = 1

while (usuario != "aluno" or senha != "123456") and cont < 3:
    print("Tente novamente.")
    cont = cont + 1
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

if usuario == "aluno" and senha == "123456":
    print("Acesso liberado")
else:
    print("Você tentou 3 vezes")
