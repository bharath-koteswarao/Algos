if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    o, t, s = 0, 0, 0
    for i in arr:
        if i == 1:
            o += 1
        else:
            t += 1
    if t == o:
        s = t
    else:
        a, b, s = 0, 0, 0
        if t > o:
            a = o
        if o > t:
            b += t
            b += (o - t) // 3
        s = max(a, b)
    print(s)
