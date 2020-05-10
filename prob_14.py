if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ar = list(arr)
    x = max(ar)
    while (ar.count(x)):
        ar.remove(x)
    print(max(ar))
