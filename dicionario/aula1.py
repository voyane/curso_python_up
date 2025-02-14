pessoas = {
    "nome" : "Voyane",
    "sexo" : "Masculino",
    "idade" : 34
}
print(pessoas)
print(pessoas["nome"])
print(f"{pessoas["nome"]}, tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())

for p, v in pessoas.items():
    print(f"{p} = {v}")