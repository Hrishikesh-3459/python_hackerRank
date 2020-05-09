from collections import Counter

x = int(input())

shoes = list(map(int, input().rstrip().split()))
count_dict = Counter(shoes)

n = int(input())

profit = 0
for i in range(n+1):
    cur = list(map(int, input().rstrip().split()))
    if (count_dict[cur[0]] != 0):
        profit += cur[1]
        count_dict[cur[0]] -= 1


print(profit)