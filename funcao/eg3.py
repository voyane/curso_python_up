def saudacao(nome):
    return f"Ola, {nome}"


mensagem = saudacao("Voyane")
print(mensagem)

def soma(a, b):
    return a + b

calculo = soma (7, 9)
print(calculo)

def par_ou_impar(numero):
    return "Par" if numero % 2 == 0 else "Impar"


numero = int(input("Digite um numero: "))
print(par_ou_impar(numero))

