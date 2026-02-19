import pandas as pd
import numpy as np

notas = np.random.uniform(low=4, high=10, size=(10, 3)).round(2)

dados = {
    'nome': ['Fernanda', 'Paula', 'Nathalye', 'Braiaw', 'Carlos', 'Fernando', 'Paulo', 'Marcos', 'Carol', 'Marinete'],
    'notas1:': notas[:, 0],
    'notas2:': notas[:, 1],
    'notas3:': notas[:, 2]
}

df = pd.DataFrame(dados)

media = df[['notas1:', 'notas2:', 'notas3:']].mean(axis=1).round(2)

# Adicionando a coluna 'media' ao DataFrame
df['media'] = media

print(df)