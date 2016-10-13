import numpy as np
import random
import matplotlib.pyplot as plt
# values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
# values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
def get_percentile(values, bucket_number):
    step = 100 / bucket_number
    return [np.percentile(values, i*step) for i in range(bucket_number)]
# print(percentiles)
# print(percentiles[len(percentiles)-1])



def get_percentile_number(value, percentiles):
    i = 0
    while value >= percentiles[i]:
        i += 1
        if i == len(percentiles):
            break
    return i - 1

# print(get_percentile_number(6, percentiles))


def value_equalization(value, percentiles, add_random=False):

    idx = get_percentile_number(value, percentiles)
    step = 1 / len(percentiles)
    if add_random == True:
        random_noise = random.uniform(0, step)
        new_value = idx * step + random_noise
    else:

        new_value = idx * step
    return new_value
# print(value_equalization(5.5, percentiles, add_random=False))


def values_equalization(values, percentiles, add_random=False):
    return [value_equalization(value, percentiles, add_random=add_random) for value in values]
# print (values_equalization(values, percentiles, add_random=False))

random.seed(0)

arr = []
with open('img.txt','r') as f:
    for line in f:
        # print(line)
        v = list(map(float,line.strip().split(" ")))
        arr.append(v)
data = np.array(arr)
# print(data)
plt.imshow(data, cmap = plt.get_cmap('gray'))


top100 = random.choice(data)
random100 = np.array(random.sample(list(data), 100))
for i in range(99):
     top100 = np.vstack([top100, random.choice(data)])

plt.subplot(321)
plt.imshow(top100, cmap = plt.get_cmap('gray'))

plt.subplot(322)
plt.imshow(random100, cmap = plt.get_cmap('gray'))

plt.subplot(323)
plt.imshow(data, cmap = plt.get_cmap('gray'))

plt.subplot(324)
plt.hist(data.flatten())

for i in range(len(data)):
     percentiles = get_percentile(data[i], 4)
     if min(data[i]) > 0: 
         percentiles[0] = 0.0
     data[i] = values_equalization(data[i], percentiles, add_random = True)
     
plt.subplot(325)
plt.imshow(data, cmap = plt.get_cmap('gray'))

plt.subplot(326)
plt.hist(data.flatten()) 

plt.show()

data = data.flatten()
print(data.mean())
