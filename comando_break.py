# n = s = 0
# while True:
#     n = int(input("Digite um numero: "))
#     if n == 999:
#         break
#     s += n
# # print("A soma e {}.".format(s)) 
# print(f"A soma e {s}.")

num = cont = soma = 0
while True:
    num = int(input("Digite um numero: "))
    
    if num == 999:
        break
    cont += 1
    soma += num
print(f"Voce digitou {cont} numeros, e a sua soma e igual a {soma}")