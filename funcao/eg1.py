def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1


valores = [2,4,6,7,8,9,0,3]
dobra(valores)
print(valores)