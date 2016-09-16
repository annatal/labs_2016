import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p1 = np.polyfit(x, y, 1)
p2 = np.polyfit(x, y, 2)
p1_f = np.poly1d(p1)
p2_f = np.poly1d(p2)
plt.plot(p1_f(x))
plt.plot(p2_f(x))
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()
plt.show()