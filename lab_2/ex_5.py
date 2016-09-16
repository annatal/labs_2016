import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0., 5., 0.1)
print('f(x)=')
a = input()
plt.xkcd()
plt.plot(eval(a))
plt.show()