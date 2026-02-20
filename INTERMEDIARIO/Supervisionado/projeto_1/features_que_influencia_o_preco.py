from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# 1. Carregamento dos dados
path = 'INTERMEDIARIO\Supervisionado\projeto_1\mercado_imobiliario_complexo.csv'
df = pd.read_csv(path)

# 2. Limpeza e Tratamento de Nulos (Pré-processamento)
df['area_m2'] = df['area_m2'].fillna(df['area_m2'].mean()).round(2)
df['vagas_garagem'] = df['vagas_garagem'].fillna(df['vagas_garagem'].mean()).round(2)
df['idade_imovel'] = df['idade_imovel'].fillna(df['idade_imovel'].mean()).round(2)
df['preco_anunciado'] = df['preco_anunciado'].fillna(df['preco_anunciado'].mean()).round(2)
df.drop_duplicates(inplace=True)  

# 3. Encoding das Colunas Categóricas (Transformando texto em números)

df['bairro'] = LabelEncoder().fit_transform(df['bairro'])
df['tipo_imovel'] = LabelEncoder().fit_transform(df['tipo_imovel'])
df['status_conservacao'] = LabelEncoder().fit_transform(df['status_conservacao'])


df['imovel_de_luxo'] = df['preco_anunciado'].apply(lambda x: 'sim' if x > df['preco_anunciado'].median() else 'nao')

df['imovel_de_luxo'] = LabelEncoder().fit_transform(df['imovel_de_luxo'])

# 4. Definição de Features e Target
features = ['bairro', 'tipo_imovel', 'area_m2', 'quartos', 'banheiros', 
                'vagas_garagem', 'idade_imovel', 'status_conservacao', 'imovel_de_luxo'] 

X = df[features]
y = df['preco_anunciado']

# 5. Divisão de Treino e Teste (80% treino, 20% teste)
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Criação do Modelo Random Forest (Melhor que a Decision Tree simples)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(train_X, train_y)

# 7. Previsões e Métricas
previsoes = model.predict(test_X)
mae = mean_absolute_error(test_y, previsoes)
r2 = r2_score(test_y, previsoes)

# --- RESULTADOS  ---

# Insight 1: O que mais influencia o preço?
importancias = pd.DataFrame({
    'Atributo': features,
    'Importância (%)': (model.feature_importances_ * 100).round(2)
}).sort_values(by='Importância (%)', ascending=False)

print("\n" + "="*40)
print(" RANKING DE INFLUÊNCIA NO PREÇO ")
print("="*40)
print(importancias)

# Insight 2: Relatório de Performance
relatorio = pd.DataFrame({
    'Valor Real': test_y.values, 
    'Previsão': previsoes.round(2), 
    'Erro Absoluto': abs(test_y.values - previsoes).round(2),
    'Erro %': (abs(test_y.values - previsoes) / test_y.values * 100).round(2)
}).sort_values(by='Erro %')

print("\n" + "="*40)
print(" RELATÓRIO DE PREVISÕES (TOP ACERTOS) ")
print("="*40)
print(relatorio.head(10))

print("\n" + "="*40)
print(f"MÉTRICAS GERAIS:")
print(f"Erro Médio (MAE): R$ {mae:,.2f}")
print(f"Score R²: {r2:.2f} (Quanto > 0.70, melhor)")
print("="*40)