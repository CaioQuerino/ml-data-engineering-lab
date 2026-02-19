import numpy as np

salarios = np.random.normal(loc=3000, scale=1000, size=400)

maxSalario = np.max(salarios)
minSalario = np.min(salarios)


print(f"Salário Máximo ==> R${maxSalario:.2f}\n")
print(f"Salário Mínimo ==> R${minSalario:.2f}")