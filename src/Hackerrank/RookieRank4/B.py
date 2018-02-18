if __name__ == '__main__':
    n = int(input().strip())
    pos = [int(_) for _ in input().strip().split()]
    hts = [int(_) for _ in input().strip().split()]
    left = True
    l = []
    for i in range(n):
        l.append((pos[i], pos[i] + hts[i]))
    l.sort(key=lambda x: (x[0], x[1]))
    maxr = l[0][1]
    for i in range(1, n):
        if l[i][0] <= maxr:
            maxr = max(maxr, l[i][1])
        else:
            left = False
            break
    left = maxr >= pos[-1]
    l = []
    for i in range(n - 1, -1, -1):
        l.append((pos[i], pos[i] - hts[i]))
    right = True
    minl = l[0][1]
    for i in range(1, n):
        if l[i][0] >= minl:
            minl = min(minl, l[i][1])
        else:
            right = False
            break
    right = minl <= pos[0]
    if left and right:
        print("BOTH")
    elif left:
        print("LEFT")
    elif right:
        print("RIGHT")
    else:
        print('NONE')
