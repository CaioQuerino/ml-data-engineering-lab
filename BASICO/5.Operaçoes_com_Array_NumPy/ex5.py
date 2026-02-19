import numpy as np

matriz_1 = np.random.randint(1, 11, size=(3,3))
matriz_2 = np.random.randint(1, 11, size=(3,3))

soma = matriz_1 + matriz_2
mult_elementos = matriz_1 * matriz_2
produto_matriz = matriz_1 @ matriz_2

print(f"Matriz A: \n {matriz_1}")
print(f"Matriz B: \n {matriz_2} \n")

print(f"Soma: \n{soma}\n")
print(f"Mult_Elementos: \n{mult_elementos}\n")
print(f"Produto_Matriz: \n{produto_matriz}")