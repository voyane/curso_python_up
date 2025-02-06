# Faca um programa que leia nome e idade de varias pessoas, guardando tudo em um lista. 
# No final, mostre quanras pessoas foram cadastradas

dados = []

dados_principal = []

while True:
    dados.append(str(input("Digite o nome: ")))
    dados.append(int(input("Digite a idade: ")))

    dados_principal.append(dados[:])
    dados_principal.clear

    resp = str(input("Quer continuar? [s/n]: "))
    if resp in "Nn":
        break
print(f"OS dado foram {dados_principal}")   

a = [1,3,5,7,8]
b = [54,76,30,99]
for item in b:
    a.append(item)
print(a)