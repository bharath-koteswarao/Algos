if __name__ == '__main__':
    s = input().strip()
    l = [s[i:j + 1] for i in range(len(s)) for j in range(i, len(s))]
    l.sort()
    s = ''.join(l)
    g = 0
    for _ in range(int(input().strip())):
        p, m = [int(i) for i in input().strip().split()]
        k = ((p * g) % m) + 1
        print(s[k - 1])
        g += ord(s[k - 1])
