print("\nQUESTÃO 9")

opcao = 0

while opcao != 3:

    print("\nMENU")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        soma = n1 + n2

        print("Resultado:", soma)

    elif opcao == 2:

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        subtracao = n1 - n2

        print("Resultado:", subtracao)

    elif opcao == 3:

        print("Programa encerrado!")

    else:

        print("Opção inválida!")
