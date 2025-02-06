listanum = []
maior = menor = 0
for n in range(0, 6):
    listanum.append(int(input("Digite um valor para a posicao {n}: ")))
    if n == 0:
        maior = menor = listanum[n]
    else:
        if listanum[n] > maior:
            maior = listanum[n]
        if listanum[n] < menor:
            menor = listanum[n]
print(f"Voce digitou os valores {listanum}")
print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")
