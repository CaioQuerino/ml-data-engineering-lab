import pandas as pd

vendas = {
    'categoria': ['Alimentos', 'Alimentos', 'Alimentos', 'Alimentos', 'Bebidas', 'Frutas', 'Frutas', 'Frutas', 'Bebidas', 'Bebidas', 'Doces', 'Doces', 'Doces'],
    'produto': ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Café', 'Maçã', 'Banana', 'Laranja', 'Refrigerante', 'Suco', 'Chocolate', 'Bala', 'Pirulito'],
    'preco': [10.50, 8.30, 5.20, 4.80, 12.00, 3.50, 2.80, 4.20, 6.50, 7.20, 5.00, 1.50, 0.80],
    'quantidade': [100, 150, 200, 120, 80, 90, 110, 75, 65, 70, 45, 60, 30],
    'data_vendas': ['2024-01-10', '2024-01-15', '2024-01-20', '2024-01-25', '2024-02-01', '2024-02-05', '2024-02-10', '2024-02-15', '2024-03-01', '2024-03-05', '2024-03-10', '2024-03-15', '2024-03-20']
}

df = pd.DataFrame(vendas)

# extrair o mes da coluna 'data_vendas' e criar uma nova coluna 'mes'
df['mes'] = pd.to_datetime(df['data_vendas']).dt.month

print(df)