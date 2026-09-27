import random

jogar_novamente = "s"

while jogar_novamente.lower() == "s":
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 20)")
    print("3 - Difícil (1 a 30)")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        minimo, maximo = 1, 10
    elif opcao == "2":
        minimo, maximo = 1, 20
    elif opcao == "3":
        minimo, maximo = 1, 30
    else:
        print("Opção inválida! Vou usar o nível Fácil (1 a 10).")
        minimo, maximo = 1, 10

    numero_sorteado = random.randint(minimo, maximo)
    tentativas = 3

    print(f"\nAdivinhe o número entre {minimo} e {maximo}. Você tem {tentativas} chances!\n")

    for tentativa in range(1, tentativas + 1):
        chute = int(input(f"Tentativa {tentativa}: Digite um número: "))

        if chute == numero_sorteado:
            print("Parabéns, você acertou!")
            break
        else:
            print("Você errou!")
            if chute < numero_sorteado:
                print("Tente um número maior")
            else:
                print("Tente um número menor")

            if tentativa == tentativas:
                print("Você perdeu! Fim de jogo.")
                print(f"O número sorteado era: {numero_sorteado}")

        print()

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")

print("\nObrigado por jogar!")
