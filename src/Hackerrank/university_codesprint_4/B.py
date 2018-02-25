from math import sqrt, ceil

if __name__ == '__main__':
    n, m = [int(__) for __ in input().strip().split()]
    ed = [int(__) for __ in input().strip().split()]
    cps = [int(__) for __ in input().strip().split()]
    rads = [int(__) for __ in input().strip().split()]
    caps = [int(__) for __ in input().strip().split()]
    cubes = []
    ma = max(rads)
    for i in range(n):
        rad = (ed[i] / sqrt(2))
        if rad < ma:
            cubes.append([ceil(rad), cps[i]])
    cyls = []
    for i in range(m):
        cyls.append([rads[i], caps[i]])
    cubes.sort(key=lambda x: x[0], reverse=True)
    cyls.sort(key=lambda x: x[0], reverse=True)
    # print(cubes, cyls)
    ans = 0
    for i in cubes:
        mi = i[0]
        copies = i[1]
        if copies == 0:
            break
        for j in range(m):
            ra = cyls[j][0]
            cap = cyls[j][1]
            if copies == 0:
                break
            else:
                if ra >= mi and cap > 0:
                    if cap >= copies:
                        cyls[j][1] -= copies
                        ans += copies
                    else:
                        i[1] -= cap
                        cyls[j][1] = 0
                        ans += cap
    print(ans)

