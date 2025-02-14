aluno = dict()
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input("Media: "))
if aluno["media"] >= 10:
    aluno["situacao"] = "Aprovado"
# elif 14 <= aluno["media"] >= 20:
#     aluno["situacao"] = "Dispensado"
else:
    aluno["situacao"] = "Reprovado"
print(aluno["situacao"])
