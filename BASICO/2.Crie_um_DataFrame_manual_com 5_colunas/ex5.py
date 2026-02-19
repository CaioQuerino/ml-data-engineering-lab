import pandas as pd
 
vendas = {
    'produto': ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Café'],
    'preco': [10.50, 8.30, 5.20, 4.80, 12.00],
    'quantidade': [100, 150, 200, 120, 80]
}

df = pd.DataFrame(vendas)

df['valor_total'] = df['preco'] * df['quantidade']

print(df)