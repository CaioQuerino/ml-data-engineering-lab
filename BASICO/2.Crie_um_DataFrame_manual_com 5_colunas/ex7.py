import pandas as pd
import numpy as np

# Configurar semente para reproduzibilidade
np.random.seed(42)

# Criar notas aleatórias
notas = np.random.uniform(low=4, high=10, size=(10, 3)).round(2)

# Criar DataFrame com alguns dados faltantes (NaN)
alunos = {
    'nome': ['Fernanda', 'Paula', 'Nathalye', 'Braiaw', 'Carlos', 'Fernando', 'Paulo', 'Marcos', 'Carol', 'Marinete'],
    'notas1': [notas[0,0], np.nan, notas[2,0], notas[3,0], np.nan, notas[5,0], notas[6,0], notas[7,0], notas[8,0], notas[9,0]],
    'notas2': [notas[0,1], notas[1,1], np.nan, notas[3,1], notas[4,1], notas[5,1], np.nan, notas[7,1], notas[8,1], notas[9,1]],
    'notas3': [notas[0,2], notas[1,2], notas[2,2], np.nan, notas[4,2], notas[5,2], notas[6,2], notas[7,2], np.nan, notas[9,2]]
}

df = pd.DataFrame(alunos)

print("="*60)
print("DataFrame ORIGINAL com dados faltantes (NaN):")
print("="*60)
print(df)
print()

# Mostrar onde estão os valores NaN
print("\nVerificando dados faltantes:")
print(df.isnull().sum())
print()

# Exercício 25: Usar .fillna() para substituir pela média da coluna
print("="*60)
print("APLICANDO .fillna() para substituir NaN pela média da coluna")
print("="*60)

# Calcular médias de cada coluna (ignorando NaN)
media_notas1 = df['notas1'].mean()
media_notas2 = df['notas2'].mean()
media_notas3 = df['notas3'].mean()

print(f"Média da coluna 'notas1': {media_notas1:.2f}")
print(f"Média da coluna 'notas2': {media_notas2:.2f}")
print(f"Média da coluna 'notas3': {media_notas3:.2f}")
print()

# Substituir NaN pela média da respectiva coluna
df_preenchido = df.copy()
df_preenchido['notas1'].fillna(media_notas1, inplace=True)
df_preenchido['notas2'].fillna(media_notas2, inplace=True)
df_preenchido['notas3'].fillna(media_notas3, inplace=True)

print("DataFrame APÓS .fillna():")
print(df_preenchido)
print()

# Calcular média de cada aluno (com dados completos)
df_preenchido['media'] = df_preenchido[['notas1', 'notas2', 'notas3']].mean(axis=1).round(2)

# Adicionar status (APROVADO/REPROVADO)
df_preenchido['status'] = df_preenchido['media'].apply(lambda x: 'APROVADO' if x >= 7 else 'REPROVADO')

print("="*60)
print("DataFrame COMPLETO com médias e status:")
print("="*60)
print(df_preenchido)
print()

print("="*60)
print("ESTATÍSTICAS DESCRITIVAS:")
print("="*60)
descricao = df_preenchido[['notas1', 'notas2', 'notas3', 'media']].describe().round(2)
print(descricao)
print()

print("="*60)
print("ANÁLISE DO STATUS:")
print("="*60)
print(df_preenchido['status'].value_counts())
print()

print("="*60)
print("DETALHES DO PREENCHIMENTO:")
print("="*60)
print("Valores que foram preenchidos com a média da coluna:")
for idx, row in df.iterrows():
    for col in ['notas1', 'notas2', 'notas3']:
        if pd.isna(row[col]):
            print(f"  {row['nome']} - {col}: NaN → {df_preenchido.loc[idx, col]:.2f} (média da coluna)")