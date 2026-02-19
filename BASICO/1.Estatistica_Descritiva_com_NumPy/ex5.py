import numpy as np

array1 = np.random.normal(loc=100, scale=20, size=500)
array2 = np.random.uniform(low=50, high=150, size=500)

mediaArray1 = np.mean(array1)
medianaArray1 = np.median(array1)

mediaArray2 = np.median(array2)
medianaArray2 = np.median(array2)

print(f"{'--'*20} Média {'--'*20}")
print(f"Array 1 {mediaArray1} | Array 2 {mediaArray2}\n")


print(f"{'--'*20} Mediana {'--'*20}")
print(f"Array 1 {medianaArray1} | Array 2 {medianaArray2}")