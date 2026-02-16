import matplotlib.pyplot as plt
import numpy as np
import random

a = np.arange(0, 2 * np.pi + 0.01, 0.01)

for i in range(20):
    r = random.uniform(0.5, 5)
    cx = random.uniform(-7, 7)
    cy = random.uniform(-7, 7)

    x = cx + r * np.cos(a)
    y = cy + r * np.sin(a)

    plt.plot(x, y)

plt.axis("equal")
plt.show()
