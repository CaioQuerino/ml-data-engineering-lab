import numpy as np

nums = np.random.normal(loc=10, scale=2, size=100) 

variancia = nums.var()
desvio_padrao = nums.std()
media = nums.mean()

coef_variacao = (desvio_padrao / media) * 100

print("-" * 35)
print(f"{'MÉTRICAS ESTATÍSTICAS':^35}")
print("-" * 35)
print(f"Média:            {media:.2f}")
print(f"Desvio Padrão:    {desvio_padrao:.2f}")
print(f"Variância:        {variancia:.2f}")
print(f"Coef. Variação:   {coef_variacao:.2f}%")
print("-" * 35)

print(f"Primeiras amostras: {nums[:5]}")
