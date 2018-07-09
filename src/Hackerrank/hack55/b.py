if __name__ == '__main__':
    n = int(input().strip())
    l = [int(__) for __ in input().strip().split()]
    r = [int(__) for __ in input().strip().split()]
    s = 0
    for i in range(n - 1):
        s += abs(min(l[i], r[i]) - min(l[i + 1], r[i + 1]))
    print(s)
