from collections import Counter

if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    s = input().strip()
    if len(set(s)) < k:
        print(0)
    else:
        co = Counter(s)
        mi = len(s)
        for x in co:
            mi = min(mi, co[x])
        if mi == 0:
            print(0)
        else:
            ans = 0
            for x in co:
                if co[x] >= mi:
                    ans += mi
            print(ans)