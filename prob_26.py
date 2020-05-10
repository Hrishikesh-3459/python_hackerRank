def merge_the_tools(string, k):
    t = []
    for i in range(0,len(string),k):
        t.append(string[i:i+k])
    u = [[] for i in range(len(t))]
    l = 0
    for i in t:
        for j in i:
            if (j not in u[l]):
                u[l].append(j)
        l += 1

    for i in u:
        for j in i:
            print(j, end="")
        print()



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
