import numpy as np
import matplotlib.pyplot as plt

nums = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(10, 6))
plt.hist(nums, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7)

plt.show()