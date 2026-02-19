import matplotlib.pyplot as plt
import numpy as np

def gerar_nums(inicio: int, fim: int, tamanho: int) -> np.ndarray:
    return np.random.randint(low=inicio, high=fim, size=tamanho)

def identidade(nums: np.ndarray) -> np.ndarray:
    return nums

def quadrado(nums: np.ndarray) -> np.ndarray:
    return nums**2


def plotar_funcoes(funcoes: list, nums: np.ndarray, cores: list = None, marcadores: list = None,
                   titulo: str = "Gráfico de Funções", xlabel: str = "x", ylabel: str = "y") -> None:
    
    plt.figure(figsize=(10, 6))
    
    # Configurar cores e marcadores padrão
    if cores is None:
        cores = ['skyblue', 'coral']
    if marcadores is None:
        marcadores = ['o', 's']
    
    # Plotar cada função com seus respectivos dados
    for i, func in enumerate(funcoes):
        y = func(nums)
        plt.scatter(nums, y, 
                   label=func.__name__,
                   color=cores[i % len(cores)],
                   marker=marcadores[i % len(marcadores)])
    
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


# Gerar dados consistentes para TODAS as funções
nums = gerar_nums(0, 10, 10)  # MESMOS dados para ambas as funções

# Chamada corrigida - passando nums como parâmetro
plotar_funcoes([identidade, quadrado], nums,
               titulo="Função Identidade e Quadrática",
               cores=["skyblue", "coral"],
               marcadores=["o", "s"])