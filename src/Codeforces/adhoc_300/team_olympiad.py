if __name__ == '__main__':
    n = int(input().strip())
    o, tw, th = 0, 0, 0
    di = {1: [], 2: [], 3: []}
    arr = [int(__) for __ in input().strip().split()]
    for i, x in enumerate(arr):
        if x == 1:
            o += 1
            di[1].append(i + 1)
        elif x == 2:
            tw += 1
            di[2].append(i + 1)
        else:
            th += 1
            di[3].append(i + 1)
    ts = min(o, tw, th)
    if ts == 0:
        print(0)
    else:
        print(ts)
        for i in range(ts):
            print(di[1][i], di[2][i], di[3][i])
