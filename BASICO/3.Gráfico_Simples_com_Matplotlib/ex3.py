import matplotlib.pyplot as plt

# Definindo os dados
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Criando o gráfico
plt.figure(figsize=(8, 5)) # Define o tamanho da imagem
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Crescimento Quadrático')

# Personalizando o gráfico
plt.title('Gráfico de Linha Simples', fontsize=14)
plt.xlabel('Eixo X (Valores)', fontsize=12)
plt.ylabel('Eixo Y (Quadrados)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6) # Adiciona uma grade suave
plt.legend()

# Exibindo o gráfico
plt.show()