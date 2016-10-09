A = [i for i in range(1,6)]

for i in range(len(A)-2, 0, -2):
    (A[i], A[i-1]) = (A[i-1], A[i])
print(*A)

B = [i for i in range(1,6)]
B = B[-1:] + B[:len(B)-1]
print(*B)

C = [1,2,2,3,3,3]
for i in C:
    if C.count(i) == 1:
        print(i)

D = [1,2,3,2,3]
max_number = 1
max_value = D[0]
for i in D:
    if D.count(i) > max_number:
        max_number = D.count(i)
        max_value = i
print(i)
