from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# 1. Carregamento dos dados
path = 'INTERMEDIARIO\Supervisionado\projeto_1\mercado_imobiliario_complexo.csv'
df = pd.read_csv(path)

# 2. Limpeza e Tratamento de Nulos
df['area_m2'] = df['area_m2'].fillna(df['area_m2'].mean()).round(2)
df['vagas_garagem'] = df['vagas_garagem'].fillna(df['vagas_garagem'].mean()).round(2)
df['idade_imovel'] = df['idade_imovel'].fillna(df['idade_imovel'].mean()).round(2)
df['preco_anunciado'] = df['preco_anunciado'].fillna(df['preco_anunciado'].mean()).round(2)

# 3. Encoding das Colunas Categóricas
le_bairro = LabelEncoder()
le_tipo = LabelEncoder()
le_status = LabelEncoder()

df['bairro'] = le_bairro.fit_transform(df['bairro'])
df['tipo_imovel'] = le_tipo.fit_transform(df['tipo_imovel'])
df['status_conservacao'] = le_status.fit_transform(df['status_conservacao'])

# 4. Definição de Features e Target 
# Importante: Incluir area_m2 para o modelo saber o que é "justo" pelo tamanho
features = ['bairro', 'area_m2', 'tipo_imovel', 'quartos', 'banheiros',] 
X = df[features]
y = df['preco_anunciado']

# 5. Divisão de Treino e Teste
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Modelo Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(train_X, train_y)
previsoes = model.predict(test_X)

# --- RESPOSTAS DE NEGÓCIO ---

# 1. Existe bairro superfaturado? 
analise_negocio = test_X.copy()
analise_negocio['preco_real'] = test_y.values
analise_negocio['preco_previsto'] = previsoes.round(2)
analise_negocio['erro_percentual'] = ((analise_negocio['preco_real'] - analise_negocio['preco_previsto']) / analise_negocio['preco_real']) * 100

# Lógica de Classificação
analise_negocio['status_mercado'] = analise_negocio['erro_percentual'].apply(
    lambda x: 'Superfaturado' if x > 20 else ('Subfaturado (Oportunidade)' if x < -20 else 'Preço Justo')
)

# Decode para leitura humana
analise_negocio['bairro_nome'] = le_bairro.inverse_transform(analise_negocio['bairro'])

print("\n" + "="*70)
print(" ANÁLISE DE PRECIFICAÇÃO E STATUS DE MERCADO ")
print("="*70)
colunas_print = ['bairro_nome', 'area_m2', 'preco_real', 'preco_previsto', 'status_mercado']
print(analise_negocio[colunas_print].sort_values(by='preco_real', ascending=False).to_string(index=False))

# 2. Casas grandes sempre são mais caras?
correlacao_area = df['area_m2'].corr(df['preco_anunciado'])

# 3. Padrão de Luxo
luxo = df[df['preco_anunciado'] > (df['preco_anunciado'].median())]

print("\n" + "="*70)
print(" DASHBOARD DE INSIGHTS (PROJETO 1 - 2026) ")
print("="*70)
print(f"-> Confiabilidade do Modelo (R²): {r2_score(test_y, previsoes):.2f}")
print(f"-> Erro Médio de Avaliação: R$ {mean_absolute_error(test_y, previsoes):,.2f}")
print(f"-> Influência da Área no Preço: {correlacao_area:.2f} (Correlação)")

if not luxo.empty:
    print(f"-> Perfil de Luxo Detectado:")
    print(f"   - Total de imóveis: {len(luxo)}")
    print(f"   - Área média: {luxo['area_m2'].mean():.2f} m²")
    print(f"   - Vagas médias: {luxo['vagas_garagem'].mean():.1f}")
else:
    print("-> Padrão de Luxo: Nenhum imóvel acima de R$ 5M encontrado no dataset.")
print("="*70)