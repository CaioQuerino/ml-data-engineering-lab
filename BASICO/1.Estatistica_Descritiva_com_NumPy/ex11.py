import numpy as np

g1 = np.random.normal(loc=50, scale=10, size=200)
g2 = np.random.normal(loc=100, scale=15, size=200)
bimodal = np.concatenate([g1, g2])

media = np.mean(bimodal)
mediana = np.median(bimodal)
desvio = np.std(bimodal)

print(f"Média:   {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio:  {desvio:.2f}")