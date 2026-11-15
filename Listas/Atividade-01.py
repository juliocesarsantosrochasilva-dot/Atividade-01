import random

nomes = []
quantidade = 0

while True:
    nome = input("Digite o nome: ")

    if nome == "fim":
        break

    nomes = nomes + [nome]
    quantidade = quantidade + 1

sorteado = random.randint(0, quantidade - 1)

print("O ganhador foi:", nomes[sorteado])
