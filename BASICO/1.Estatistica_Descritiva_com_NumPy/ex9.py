import numpy as np

nums = np.random.normal(loc=0, scale=1, size=100)


op = (nums - nums.mean()) / nums.std()


nova_media = op.mean()
novo_desvio = op.std()

print("-" *40)
print(f"Média original: {nums.mean():.4f}")
print(f"Desvio original: {nums.std():.4f}")
print("-" * 40)
print(f"Nova Média (após padronização): {nova_media:.4f}")
print(f"Novo Desvio (após padronização): {novo_desvio:.4f}")
print("-" * 40)