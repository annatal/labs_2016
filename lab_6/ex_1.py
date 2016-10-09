import random
import matplotlib.pyplot as plt
N=[100, 1000, 10000, 100000]
random.seed(0)
for i in range(0, len(N)):
    plt.subplot(220 + i+1)
    values = [random.normalvariate(0, 1) for k in range(N[i])]
    plt.hist(values, bins=100)

plt.show()
