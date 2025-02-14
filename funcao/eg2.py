# def nome_da_funcao(parametro):
#     #instrucao1
#     #instrucao2
#     #...
#     #return valor (opcional)

#funcao sem parametro e sem retorno
def saudacao():
    print("Ola mundo!!!!")

saudacao()

#Com parametro
def cumprimentar(nome):
    print(f"Ola, {nome}")

cumprimentar("Voyane")

#com retorno
def soma(a, b):
    return a + b

resultado = soma(3, 6)
print(resultado)

def dobro(num):
    return num * 2

resul = dobro(7)
print(resul)