soma = 0
cont = 0
maior = 0

num = int(input("Digite um número: "))

while num >= 0:
    soma = soma + num
    cont = cont + 1

    if num > maior:
        maior = num

    num = int(input("Digite um número: "))

if cont > 0:
    media = soma / cont
    print("Soma:", soma)
    print("Média:", media)
    print("Maior número:", maior)
else:
    print("Nenhum número positivo foi informado.")
