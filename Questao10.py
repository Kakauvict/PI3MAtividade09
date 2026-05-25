print("\nQUESTÃO 10")

orcamento = float(input("Digite o orçamento máximo: "))

total_gasto = 0

gasto = float(input("Digite um gasto: "))

while gasto >= 0 and total_gasto <= orcamento:

    total_gasto = total_gasto + gasto

    if total_gasto > orcamento:
        print("Orçamento excedido!")
        break

    gasto = float(input("Digite outro gasto: "))

sobrou = orcamento - total_gasto

print("Total gasto:", total_gasto)
print("Sobrou:", sobrou)
