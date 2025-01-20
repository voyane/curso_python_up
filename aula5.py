#LOOP FOR

for i in range(0, 5): #executa funcao e inprime valores de i no intervalo de 0 a 4
    print(i*2)

soma = 0
for j in range (1, 101): #Calcula a soma dos numeros de 1 a 100.
    soma +=1
    print(soma)   

frutas = ["maca", "banana", "laranja", "maca", "uva", "maca"]
contagem = 0
for fruta in frutas:
    if fruta == "maca":
        contagem = contagem + 1
print("A", fruta, "aparece", contagem, "vezes") 


num = int(input("Digite um numero: "))
for cont in range(0,13):
    cont +=1
    print(num, "X", cont, "=", num*cont)