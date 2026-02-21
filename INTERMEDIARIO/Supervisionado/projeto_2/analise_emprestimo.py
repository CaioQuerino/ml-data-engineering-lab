import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

path = 'INTERMEDIARIO/supervisionado/projeto_2/clientes_banco.csv'
df = pd.read_csv(path)

df['risco_inadimplencia'] = (df['divida_atual'] > (df['renda'] * 2)).astype(int)

y = df['risco_inadimplencia']


features = ['idade', 'renda', 'score_credito', 'divida_atual', 'tempo_emprego']
X = df[features]

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=42)


rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(train_X, train_y)

previsions = rf.predict(test_X)
train_acc = accuracy_score(train_y, rf.predict(train_X))
test_acc = accuracy_score(test_y, previsions)

print(f'{"="*45}')
print(" MODELO DE PREVISÃO DE RISCO DE CRÉDITO ")
print(f'{"="*45}')
print(f"Acurácia no Treino: {train_acc:.2f}")
print(f"Acurácia no Teste: {test_acc:.2f}")
print("-" * 45)

# Teste do novo cliente: [Idade, Renda, Score, Divida, Tempo Emprego]
novo_cliente = [[30, 5000, 700, 12000, 5]] 
resultado = rf.predict(novo_cliente)

status = "RISCO ALTO (Negar)" if resultado[0] == 1 else "RISCO BAIXO (Aprovar)"
print(f"\nResultado para o Novo Cliente: {status} \n")


importancias = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=False)
print("Importancia das features concideradas:")
print(importancias)
