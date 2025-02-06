valores = [] #list()
valores.append(7)
valores.append(9)
valores.append(30)

for valor in valores:
    print(valor, "...", end= " ")

for c, v in enumerate(valores):
    print(f"Na posicao {c}, encontrei o valor {v}")

#ler pelo teclado e colocar dentro da lista

val = list()
for cont in range (0, 5):
    cont = int(input("Digite um valor: "))
