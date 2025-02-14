def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.12
    else:
        imposto = valor  * 0.2
    return imposto

preco_do_produto = 2500
imposto_produto = calcular_imposto(preco_do_produto)
print(imposto_produto)