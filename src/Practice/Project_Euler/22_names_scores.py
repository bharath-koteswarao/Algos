if __name__ == '__main__':
    n = int(input().strip())
    l = []
    for i in range(n):
        l.append(input().strip())
    l = sorted(l)
    q = int(input().strip())
    for i in range(q):
        name = input().strip()
        mul = l.index(name) + 1
        total = 0
        for j in name:
            total += (ord(j) - ord('A') + 1)
        print(mul * total)