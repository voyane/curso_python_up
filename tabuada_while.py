while True:
    num = int(input("Digite um numero inteiro: "))
    if num < 0:
        break
    print("=" * 40)
    for c in range(1, 11):
        print(f"{num} X {c} = {num*c}")
    print("=" * 40)
print("Programa encerrado... Volte sempre.")