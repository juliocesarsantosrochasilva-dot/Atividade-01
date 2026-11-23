
# JOGO DE ADIVINHACAO DE PALAVRAS

palavra = "PYTHON"

letras_descobertas = []
letras_utilizadas = []

erros = 0
limite_erros = 6
venceu = False

print("=" * 35)
print("       JOGO DE ADIVINHACAO")
print("=" * 35)

while erros < limite_erros:

    print("\nPalavra: ", end="")

    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"\nErros: {erros}/{limite_erros}")

    venceu = True

    for letra in palavra:
        if letra not in letras_descobertas:
            venceu = False

    if venceu:
        break

    letra = input("Digite uma letra: ").upper()

    if letra == "":
        print("Digite uma letra!")

    elif letra in letras_utilizadas:
        print("Letra já utilizada!")

    else:
        letras_utilizadas = letras_utilizadas + [letra]

        if letra in palavra:
            print("Acertou!")
            letras_descobertas = letras_descobertas + [letra]
        else:
            print("Errou!")
            erros = erros + 1

print("\n" + "=" * 35)

if venceu:
    print("Você venceu!")
else:
    print("Você perdeu!")

print(f"A palavra era: {palavra}")

print("=" * 35)
