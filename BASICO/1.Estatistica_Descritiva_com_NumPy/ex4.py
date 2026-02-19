import numpy as np

nums = np.random.normal(loc=0, scale=1, size=1000)

count1 = np.sum(nums > 1.96)
count2 = np.sum(nums < -1.96)

print(f"Números acima de 1,96 é igual a {count1}")
print(f"Números abaixo de -1,96 é igual a {count2}")