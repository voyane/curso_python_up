cont = []  # Lista para armazenar os números inseridos
resp = "s"

while True:
    numero = int(input("Digite um número: "))
    cont.append(numero)  # Adiciona o número à lista
    resp = input("Deseja continuar? [s/n]: ").strip().lower()  # Remove espaços e converte para minúsculo
    
    if resp == "s":
        continue  # Volta ao início do loop para pedir outro número
    elif resp == "n":
        break  # Sai do loop e encerra o programa
    else:
        print("Opção inválida! Por favor, digite 's' para continuar ou 'n' para encerrar.")

# Exibe todos os números digitados
print(f"Os números inseridos são: {cont}")