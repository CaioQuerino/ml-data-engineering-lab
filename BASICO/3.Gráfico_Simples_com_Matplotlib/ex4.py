import matplotlib.pyplot as plt
import numpy as np

def gerar_nums(inicio: int, fim: int, quantidade: int) -> np.ndarray :
    """Gera números inteiros aleatórios dentro de um intervalo.
    
    Args:
        inicio: Valor mínimo (inclusive)
        fim: Valor máximo (exclusive)
        quantidade: Número de valores a gerar
        
    Returns:
        Array NumPy com números inteiros aleatórios
    """
    return np.random.randint(low=inicio, high=fim, size=quantidade)


nums = gerar_nums(0, 10, 10)

plt.figure(figsize=(10, 6))
plt.scatter(nums, nums**2)
plt.xlabel("Valores")
plt.ylabel("Quadrados")
plt.title("Gráfico de Quadrados")
plt.grid(True)
plt.show()