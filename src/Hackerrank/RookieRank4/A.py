if __name__ == '__main__':
    n, mt = [int(i) for i in input().strip().split()]
    l = []
    for _ in range(n):
        l.append(int(input().strip()))
    l.sort()
    i = 0
    while mt - l[i] >= 0 and i < n:
        mt -= l[i]
        i += 1
    print(i)
