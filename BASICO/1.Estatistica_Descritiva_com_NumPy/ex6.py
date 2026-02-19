import numpy as np

alturas = np.random.normal(loc=1.70, scale=0.10, size=300)

alturasCm = np.multiply(alturas, 100)

percentis = np.percentile(alturasCm, [25, 50, 75])

p25 = percentis[0]
p50 = percentis[1]
p75 = percentis[2]

print(f"Relatório de Alturas (cm):")
print(f"Média: {alturasCm.mean():.2f} cm")
print(f"P25:   {p25:.2f} cm")
print(f"P50:   {p50:.2f} cm (Mediana)")
print(f"P75:   {p75:.2f} cm")