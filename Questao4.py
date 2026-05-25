print("\nQUESTÃO 4")

idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 150:
    print("Idade inválida!")
    idade = int(input("Digite novamente: "))

print("Idade válida:", idade)
