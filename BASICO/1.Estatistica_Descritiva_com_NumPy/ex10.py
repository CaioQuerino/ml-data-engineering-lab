import numpy as np

np.set_printoptions(precision=2, suppress=True)

def calcular_estatisticas(loc: float, scale: float, size: int) -> np.ndarray:
    nums = np.random.normal(loc=loc, scale=scale, size=size)
    
    media = np.mean(nums)
    mediana = np.median(nums)
    maximo = np.max(nums)
    minimo = np.min(nums)
    variacao = np.var(nums)
    desvio = np.std(nums)

    return np.array([media, mediana, maximo, minimo, variacao, desvio])

result = calcular_estatisticas(loc=3000, scale=1000, size=300)

print(result)