cont = ("zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", "onze", 
    "doze", "treze", "quatorze", "quinze", "dezesseis", 
    "dezessete", "dezoito", "dezenove", "vinte")
#resp = "S"
while True:
 #   if resp == "S":
        num = int(input("Digite um numero de 0 a 20: "))
 #       resp = str(input("VOce deseja continuar?[S/N]: ")).upper()
        if num >= 0 and num <= 20:
            break
        print("Tente novamente.")
print(f"O numero digitado e: {cont[num]}")