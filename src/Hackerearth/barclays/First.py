if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    k = int(input().strip())
    l = []
    for i in s1:
        l.append(ord(i) - 96)
    for i in s2:
        l.append(ord(i) - 96)
    l.sort()
    l += l
    pre = []
    # (pro,start,end)
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            pre.append(((l[j] - l[i]) * (j - i), i, j))
    print(len(pre))
