for _ in range(int(input().strip())):
    n = int(input().strip())
    lis = [int(i) for i in input().strip().split()]
    ans = {0: 0, 1: 0}
    lis.reverse()
    ap = None
    degree = n
    for i in lis:
        if i != 0:
            ap = i
            break
        else:
            degree -= 1
    if ap == None:
        pass
    elif ap > 0:
        ans[0] = 1
        if degree % 2 == 0:
            ans[1] = 1
        else:
            ans[1] = -1
    elif ap < 0:
        ans[0] = -1
        if degree % 2 == 0:
            ans[1] = -1
        else:
            ans[1] = 1
    print(ans[0], end=" ")
    print(ans[1])
