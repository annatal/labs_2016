lines=[]
with open('input_4.txt', 'r') as f:
    for line in f:
        print(line)
        # lines.append(line)
        lines +=[line.rstrip()]
        # print(a, b)

print(lines)
A = list(map(int, lines[0].split()))
# print(list(map(int, lines[0].split())))
print(A)
print(lines[0])
print(lines[1])
