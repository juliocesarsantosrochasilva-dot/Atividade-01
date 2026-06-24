funcionario = input("Digite o seu cargo: ")
salario = float(input("Digite o seu salário: "))

if funcionario == "programador de sistemas ":
    salario = salario * 1.30

elif funcionario == "analista de sistema ":
    salario = salario * 1.20

elif funcionario == "Analista de bancos de dados":
    salario = salario * 1.15

else:
    print("Cargo inválido!")

print("Novo salário:", salario)
