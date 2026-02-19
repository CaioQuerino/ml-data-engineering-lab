import pandas as pd
import numpy as np

notas = np.random.uniform(low=4, high=10, size=(10, 3)).round(2)

alunos = {
    'nome': ['Fernanda', 'Paula', 'Nathalye', 'Braiaw', 'Carlos', 'Fernando', 'Paulo', 'Marcos', 'Carol', 'Marinete'],
    'notas1:': notas[:, 0],
    'notas2:': notas[:, 1],
    'notas3:': notas[:, 2]
}

df = pd.DataFrame(alunos)

media = df[['notas1:', 'notas2:', 'notas3:']].mean(axis=1).round(2)

df['media'] = media

# Adicionando a coluna 'status' ao DataFrame
# A função lambda é usada para atribuir 'APROVADO' se a média for maior ou igual a 7, caso contrário, 'REPROVADO'.
df['status'] = df['media'].apply(lambda x : 'APROVADO' if x >= 7 else 'REPROVADO')

filtro = (df['status'] == "APROVADO") & (df['media'] >= 7) & (df['notas1:'] > 6)

print(media.groupby(df['media']).mean())