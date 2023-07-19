usuarios_data_science = {15, 23, 45, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# Set representa um conjunto sem elementos repetidos
# Conjuntos não tem ordem, index

assistiram = usuarios_data_science.copy()
# assistiram.extend(usuarios_machine_learning)

# for usuario in set(assistiram):
#     print(usuario)

print( usuarios_data_science | usuarios_machine_learning)
