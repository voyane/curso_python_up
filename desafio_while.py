# resp = "S"
# sexo = str(input("Qual e o sexo?: ")).upper()
# while sexo not in "MF":
#     sexo = str(input("Dados invalido. Por favor, insira o sexo correctamente.")).upper()
#     resp = str(input("Quer continuar?[S/N]: "))    
# print("Sexo {} registado com sucesso.".format(sexo))

from random import randint
computador = randint (0, 10)
print("Sou o computador... Acabei de pensar num numero entre 0 e 10")
print("Voce consegue adivinhar que numero e'? ")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Pense num numero entre 0 e 10.: "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais, tente mais uma vez.")
        else:
            print("Menos, tente mais uma vez.")
print("Acertou!!!")