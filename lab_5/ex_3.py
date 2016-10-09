A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])

B = []
for i in range(len(A)):
    print(i, len(A)-i)
    B.append(A[i])
    B.append(A[len(A)-1-i])

print(*B[:len(A)])
