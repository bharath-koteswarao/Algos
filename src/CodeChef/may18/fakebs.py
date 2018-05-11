"""
1
7 7
3 1 6 7 2 5 4
1
2
3
4
5
6
7

1
7 1
10 3 5 2 1 0 8
1
"""
if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, q = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        idx = {}
        sor = {}
        std = sorted(arr)
        for __ in range(n):
            sor[std[__]] = __
        for __ in range(n):
            idx[arr[__]] = __
        for __ in range(q):
            x = int(input().strip())
            lc, rc = sor[x], n - sor[x] - 1
            ind = idx[x]
            low, high = 0, n - 1
            lswaps, rswaps = 0, 0
            possible = True
            while low <= high:
                mid = (low + high) // 2
                middle = arr[mid]
                if x == middle:
                    break
                elif x < middle:
                    if ind < mid:
                        high = mid - 1
                    else:
                        if lc > 0:
                            lswaps += 1
                            lc -= 1
                            low = mid + 1
                        else:
                            possible = False
                            break
                else:
                    if ind > mid:
                        low = mid + 1
                    else:
                        if rc > 0:
                            rswaps += 1
                            rc -= 1
                            high = mid - 1
                        else:
                            possible = False
                            break
            print(max(lswaps, rswaps) if possible else -1)