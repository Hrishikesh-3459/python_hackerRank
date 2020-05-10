# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

x = input()

l = x.split()

s = str(l[0])

k = int(l[1])


for i in list(sorted((permutations(list(s),k)))):
    for j in i:
        print(j, end = "")

    print()

