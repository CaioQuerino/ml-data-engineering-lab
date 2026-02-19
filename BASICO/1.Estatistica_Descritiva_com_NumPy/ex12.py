import numpy as np
 
def gerar_matriz(low: float, high: float, a: int, b: int) -> np.ndarray :
    return np.random.randint(low=low, high=high, size=(a, b))

matriz_1 = gerar_matriz(1, 20, 4, 4)
matriz_2 = gerar_matriz(1, 20, 4, 4)

soma = matriz_1 + matriz_2
subtracao = matriz_1 - matriz_2
multiplicacao = matriz_1 * matriz_2

print(f"{'--' * 10} SOMA {'--' * 10}")
print(f"\n {soma} \n")

print(f"{'--' * 10} SUBTRAÇÃO {'--' * 10}")
print(f"\n {subtracao} \n" )

print(f"{'--' * 10} MULTIPLICAÇÃO {'--' * 10}")
print(f"\n {multiplicacao} \n" )