import pandas as pd

produtos = {
    'categoria': ['Alimentos', 'Alimentos', 'Alimentos', 'Alimentos', 'Bebidas', 'Frutas', 'Frutas', 'Frutas', 'Bebidas', 'Bebidas', 'Doces', 'Doces', 'Doces'],
    'produto': ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Café', 'Maçã', 'Banana', 'Laranja', 'Refrigerante', 'Suco', 'Chocolate', 'Bala', 'Pirulito'],
    'preco': [10.50, 8.30, 5.20, 4.80, 12.00, 3.50, 2.80, 4.20, 6.50, 7.20, 5.00, 1.50, 0.80],
    'quantidade': [100, 150, 200, 120, 80, 90, 110, 75, 65, 70, 45, 60, 30],
}

df = pd.DataFrame(produtos)

df = df.groupby('categoria').get_group('Doces')

df['valor_total'] = df['preco'] * df['quantidade']

print(df)