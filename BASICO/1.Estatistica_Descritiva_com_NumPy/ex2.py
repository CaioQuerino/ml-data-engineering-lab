import numpy as np

nums = np.random.normal(loc=75, scale=15, size=200)

media = np.mean(nums)
mediana = np.median(nums)
desvio_padrao = np.std(nums)

print(f"Média ==> {media}")
print(f"Mediana ==> {mediana}")
print(f"Desvio Padrão ==> {desvio_padrao}")