import pandas as pd

dados = {
    "nome": ["Nathalia",  "Fernanda", "Paula", "Laryssa", "Fernando", "Matheus", "João", "Pedro", "Carlos", "Antonia"],
    "idade": [20, 18, 19, 35, 33, 40, 50, 15, 24, 26],
    "cidade": ["RJ", "SP", "MG", "RJ", "RJ", "SP", "ES", "MS", "RJ", "RJ"],
    "salario": [1385.95, 1560.75, 1256.95, 2550.75, 5550.00, 5550.75, 5550.75, 5550.75, 5550.75, 5550.75],
    "departamento": ["TI", "RH", "Vendas", "TI", "Financeiro", "RH", "Vendas", "Diretoria", "TI", "Marketing"]
}

df = pd.DataFrame(dados)

relatorio = df.agg({
    'salario': 'max',
    'idade': 'min',
    'nome': 'count'
})

relatorio.index = ['Salário Máximo', 'Idade Mínima', 'Qtde Funcionários']

print(relatorio)