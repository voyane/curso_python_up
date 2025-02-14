aluno = dict()
aluno["nome"] = str(input("Digite o nome do aluno: "))
aluno["nota1"] = float(input("Digite a primeira nota: "))
aluno["nota2"] = float(input("Digite a segunda nota: "))
aluno["media"] = (aluno["nota1"] + aluno["nota2"]) / 2
if aluno["nota1"] > 20:
    print("Nota invalida. Por favor, retifique")
elif aluno["nota2"] > 20:
    print("Nota invalida. Por favor, retifique")
else:
    if aluno["media"] >= 10 and aluno["media"] <= 13.4:
        aluno["situacao"] = "Aprovado"
    elif aluno["media"] >= 13.5 and aluno["media"] <= 20:
        aluno["situacao"] = "Dispensado"
    else:
        aluno["situacao"] = "Reprovado"

print("=-=" *20)
print(f"O aluno {aluno['nome']} teve media {aluno['media']}")
print(f"Ele esta {aluno['situacao']}")
print("=-=" *30)