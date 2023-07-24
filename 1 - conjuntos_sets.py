usuarios_data_science = {15, 23, 45, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# Set representa um conjunto sem elementos repetidos
# Conjuntos não tem ordem, index

assistiram = usuarios_data_science.copy()

# assistiram.extend(usuarios_machine_learning)

# for usuario in set(assistiram):
#     print(usuario)

# Itens que são únicos entre os conjuntos
print(usuarios_data_science | usuarios_machine_learning)

# Itens que estão em ambos conjuntos
print(usuarios_data_science & usuarios_machine_learning)

# Está no primeiro mas não esta no segundo
print(usuarios_data_science - usuarios_machine_learning)


fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(15 in fez_ds_mas_nao_fez_ml)
print(23 in fez_ds_mas_nao_fez_ml)

# Está em um dos conjuntos mas não nos dois
print(usuarios_data_science ^ usuarios_machine_learning)
