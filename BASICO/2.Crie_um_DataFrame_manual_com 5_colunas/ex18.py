import pandas as pd

dados = {
    "nome": ["Nathalia",  "Fernanda", "Paula", "Laryssa", "Fernando", "Matheus", "João", "Pedro", "Carlos", "Antonia", 'Maria'],
    "idade": [20, 18, 19, 35, 33, 40, 50, 15, 24, 26, 60],
    "cidade": ["RJ", "SP", "MG", "RJ", "RJ", "SP", "ES", "MS", "RJ", "RJ", "RJ"],
    "salario": [1385.95, 1560.75, 1256.95, 2550.75, 5550.00, 5550.75, 5550.75, 5550.75, 5550.75, 5550.75, 3000.00],
    "departamento": ["TI", "RH", "Vendas", "TI", "Financeiro", "RH", "Vendas", "Diretoria", "TI", "Marketing", "Financeiro"]
}

df = pd.DataFrame(dados)

df['bonus'] = df.apply(lambda x : x['salario'] * 0.10 if x['cidade'] == 'RJ' else x['salario'] * 0.05, axis=1).round(2)

print(df)