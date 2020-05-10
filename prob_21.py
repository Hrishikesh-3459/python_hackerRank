def mutate_string(string, position, character):
    y = list(string)
    y.pop(position)
    y.insert(position, character)
    return(''.join(y))

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
