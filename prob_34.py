n = int(input())
N = []
for i in range(n):
    N.append(list(input()))
b = int(input())
B = []
for i in range(b):
    B.append(list(input()))
N = set(N)
B = set(B)
print(N.union(B))
