import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-4, 4.01, 0.0005)
plt.plot(x, x*x - x - 6)
plt.grid(True)
plt.show()
x1 = -2
x2 = 3