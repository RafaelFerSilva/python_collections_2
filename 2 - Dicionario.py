from collections import defaultdict
from collections import Counter

# aparicoes = {
#     "Guilherme": 1,
#     "cachorro": 2,
#     "nome": 2,
#     "vindo": 1
# }
#
# print(aparicoes.get("cachorro", 0))
#
# # Criar um dicionário
# aparicoes2 = dict(Guilherme = 2, cachorro = 1)
#
# aparicoes["Carlos"] = 1
#
# print(aparicoes)
#
# del aparicoes["Carlos"]
#
# print(aparicoes)
#
# print("cachorro" in aparicoes)
#
# print("Carlos" in aparicoes)
#
#
# for elemento in aparicoes:
#     print(elemento)
#
#
# for elemento in aparicoes.values():
#     print(elemento)
#
#
# for elemento in aparicoes.keys():
#     valor = aparicoes[elemento]
#     print(elemento, valor)
#
# for elemento in aparicoes.items():
#     print(elemento)
#
#
# for chave, valor in aparicoes.items():
#     print(chave, " = ", valor)
#
#
# ["palavra {}".format(chave) for chave in aparicoes.keys()]


# meu_texto = "Bem vindo meu nome é Rafael eu gosto muito de notas e tenho meu cachorro e gosto muito de cachorro"
# meu_texto = meu_texto.lower()
# print(meu_texto)
#
# aparicoes = defaultdict(int)
# for palavra in meu_texto.split():
#     ate_agora = aparicoes[palavra]
#     aparicoes[palavra] = ate_agora + 1
#
# print(aparicoes)


meu_texto = "Bem vindo meu nome é Rafael eu gosto muito de notas e tenho meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
print(meu_texto)

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)


class Conta:
    def __init__(self):
        print("Criando uma Conta")


contas = defaultdict(Conta)
print(contas[15])
print(contas[17])
print(contas[15])


aparicoes = Counter()
for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)


aparicoes = Counter(meu_texto.split())

print(aparicoes)




