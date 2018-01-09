if __name__ == '__main__':
    n = int(input().strip())
    l1, l2 = [], []
    s1, s2 = 0, 0
    for i in range(n, 0, -1):
        if s1 < s2:
            s1 += i
            l1.append(i)
        else:
            s2 += i
            l2.append(i)
    print(abs(s1 - s2))
    print(len(l1), end=" ")
    for i in l1:
        print(i, end=" ")
