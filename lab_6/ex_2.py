import random
a= -2
b = 2
N = 1000000
sum = 0
def f(x):
    # if -2<=x<=2:
        return -x**2 + 4
    # else:
    #     return 0
for i in range (1,N):
    x = random.uniform(a, b)
    sum = sum + f(x)
print(sum)
integr =(b - a)*sum/N
print(integr)
