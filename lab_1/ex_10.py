S = input()
a = S.count('h')
P = S.replace('h', 'H', a-1)
print(P.replace('H', 'h',1))
