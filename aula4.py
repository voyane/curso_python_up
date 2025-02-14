#Condicoes if
ano = int(input("Digite o seu ano de nascimento: "))
idade = 2025 - ano
if idade >= 18:
    print("Voce e maior de idade")
else: 
    print("voce e menor de idade.".capitalize())