from bisect import bisect_left as bs

if __name__ == '__main__':
    n = int(input().strip())
    pos = [int(_) for _ in input().strip().split()]
    hts = [int(_) for _ in input().strip().split()]
    left = True
    nex = 0
    i = 0
    while True:
        nex = bs(pos, pos[i] + hts[i])
        if nex >= n:
            break
        else:
            if pos[i] + hts[i] < pos[nex]:
                left = False
                break
            i += 1
    right = True
    nex = n - 1
    i = n - 1
    while True:
        nex = bs(pos, pos[i] - hts[i])
        if nex == 0:
            break
        else:
            if pos[i] - hts[i] > pos[nex]:
                right = False
                break
            i -= 1
    if left and right:
        print("BOTH")
    elif left:
        print("LEFT")
    elif right:
        print("RIGHT")
    else:
        print('NONE')
