import numpy as np
import matplotlib.pyplot as plt

def gerar_nums(loc: float, scale: float, size: int) -> np.ndarray[np.float64, np.dtype[np.float64]] :
    return np.random.normal(loc=loc, scale=scale, size=size)


def plotar_graphic(x: np.ndarray, y: np.ndarray) -> None :
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, marker="o", color="gray", label="Pontos aleatórios")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    plt.grid(True, alpha=0.3)
    
    plt.show()


x = gerar_nums(0, 1, 100)
y = gerar_nums(0, 1, 100)

plotar_graphic(x, y)