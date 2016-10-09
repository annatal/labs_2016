a = int(input())
A = [i+1 for i in range(a)]
print(A)

k = [i**2 for i in A if i % 3 == 1 and i < a]
print(sum(k))
