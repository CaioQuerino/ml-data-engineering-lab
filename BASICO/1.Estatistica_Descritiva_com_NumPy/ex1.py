import numpy as np

# Seus dados
nums = np.random.normal(loc=50, scale=10, size=100)

media = np.mean(nums)   
mediana = np.median(nums)
desvio = np.std(nums)
variancia = np.var(nums)
minimo = np.min(nums)
maximo = np.max(nums)

print("-" * 40)
print(f"{'RELATÓRIO ESTATÍSTICO':^40}")
print("-" * 40)

print(f"Média:      {media:>10.2f}")
print(f"Mediana:    {mediana:>10.2f}")
print(f"Desvio P.:  {desvio:>10.2f}")
print(f"Variância:  {variancia:>10.2f}")

print("-" * 40)
print(f"Mínimo: {minimo:.2f}   |   Máximo: {maximo:.2f}")
print("-" * 40)