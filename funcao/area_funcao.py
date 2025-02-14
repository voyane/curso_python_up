def area(larg, comp):
    a = larg * comp
    print(f"A area do terreno {larg}X{comp} e de {a}m2.")


l = float(input("Largura: "))
c = float(input("Comprimento: "))
area(l, c)