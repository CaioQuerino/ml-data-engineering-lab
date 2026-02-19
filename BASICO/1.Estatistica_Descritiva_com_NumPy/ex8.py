import numpy as np

temperaturas = np.random.normal(loc=22, scale=5, size=365)
dias_quentes = np.sum(temperaturas > 30)

print(f"Número de dias com temperatura > 30°C: {dias_quentes}")