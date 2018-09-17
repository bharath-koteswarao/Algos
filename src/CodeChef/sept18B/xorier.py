from collections import Counter
from math import factorial as fact


def nCr(n, r):
    if n == 0:
        return 0
    elif r == 0:
        return 1
    return int(fact(n) / (fact(r) * fact(n - r)))


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = [int(__) for __ in input().strip().split()]
        co = Counter(arr)
        e, o = 0, 0
        for x in arr:
            if x % 2 == 0:
                e += 1
            else:
                o += 1
        ans = 1
        for x in co:
            ans *= co[x]
        invalid = []
        re = 0
        for x in co:
            if x ^ 2 in co:
                invalid.append([x, x ^ 2])
        for inv in invalid:
            re += co[inv[0]] * co[inv[1]]
        print(ans - re // 2)
