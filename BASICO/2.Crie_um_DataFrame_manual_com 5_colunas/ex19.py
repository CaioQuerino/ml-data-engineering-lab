import pandas as pd

# DataFrame 1: Funcionários
funcionarios = pd.DataFrame({
    "id_func": [1, 2, 3, 4, 5, 6, 7, 8],
    "nome": ["Nathalia", "Fernanda", "Paula", "Laryssa", "Fernando", "Matheus", "João", "Pedro"],
    "idade": [20, 18, 19, 35, 33, 40, 50, 15],
    "salario": [1385.95, 1560.75, 1256.95, 2550.75, 5550.00, 5550.75, 5550.75, 5550.75],
    "id_depto": [101, 102, 103, 101, 104, 102, 103, 105]
})

# DataFrame 2: Departamentos
departamentos = pd.DataFrame({
    "id_depto": [101, 102, 103, 104, 105, 106],
    "nome_depto": ["TI", "RH", "Vendas", "Financeiro", "Diretoria", "Marketing"],
    "gerente": ["Carlos", "Ana", "Roberto", "Mariana", "Sérgio", "Beatriz"],
    "orcamento_anual": [50000, 30000, 45000, 80000, 120000, 35000]
})

df_inner = pd.merge(funcionarios, departamentos, on='id_depto', how='inner')

print(df_inner)