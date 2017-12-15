if __name__ == '__main__':
    st = input().strip()
    q = int(input().strip())
    for _ in range(q):
        a, b = input().strip().split(" ")
        a = int(a)
        a -= 1
        st = st[:a] + b + st[a + 1:]
    m = int(input().strip())
    print(st)
    s = st[:]
    for _ in range(m):
        a, b = [int(i) for i in input().strip().split(" ")]
        a, b = a - 1, b - 1
        st = st[:a] + st[a:b + 1][::-1] + st[b + 1:]
    c = 0
    print(st)
    for i in range(len(st)):
        if s[i] == st[i]:
            c += 1
    print(c)
