import matplotlib.pyplot as plt
import pandas as pd

def plotar_graphic(vendas: pd.Series, produto: pd.Series, titulo: str, xlabel: str, ylabel: str) -> None :
    plt.figure(figsize=(10, 6))

    plt.bar(produto, vendas)

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()

vendas = {
    'categoria': ['Alimentos', 'Alimentos', 'Alimentos', 'Alimentos', 'Bebidas'],
    'produto': ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Café'],
    'preco': [10.50, 8.30, 5.20, 4.80, 12.00],
    'quantidade': [100, 150, 200, 120, 80],
    'data_vendas': ['2024-01-10', '2024-01-15', '2024-01-20', '2024-01-25', '2024-02-01']
}

df = pd.DataFrame(vendas)

df['vendas'] = df['preco'] * df['quantidade']


plotar_graphic(df['vendas'], df['produto'], "Faturamento por produto", "Produto", "Faturamento")