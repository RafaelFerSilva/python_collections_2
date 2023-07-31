aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

print(aparicoes.get("cachorro", 0))

# Criar um dicionário
aparicoes2 = dict(Guilherme = 2, cachorro = 1)

aparicoes["Carlos"] = 1

print(aparicoes)

del aparicoes["Carlos"]

print(aparicoes)

print("cachorro" in aparicoes)

print("Carlos" in aparicoes)


for elemento in aparicoes:
    print(elemento)


for elemento in aparicoes.values():
    print(elemento)


for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

for elemento in aparicoes.items():
    print(elemento)


for chave, valor in aparicoes.items():
    print(chave, " = ", valor)


["palavra {}".format(chave) for chave in aparicoes.keys()]