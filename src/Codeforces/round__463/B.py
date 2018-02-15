from bisect import bisect_left as bs


def f(x):
    pr = 1
    while x > 0:
        re = x % 10
        if re > 0:
            pr *= re
        x //= 10
    return pr


def g(x, memo):
    if x in memo:
        return memo[x]
    else:
        if x < 10:
            memo[x] = x
            return memo[x]
        else:
            memo[x] = g(f(x), memo)
            return memo[x]


if __name__ == '__main__':
    lis = []
    memo = {}
    ans = {key: [] for key in range(1, 10)}
    for i in range(1, 10 ** 6 + 1):
        lis.append(g(i, memo))
    for i in range(len(lis)):
        ans[lis[i]].append(i + 1)
    print(ans)
    for _ in range(int(input().strip())):
        l, r, k = [int(i) for i in input().strip().split()]
        ar = ans[k]
        if len(ar) == 0:
            print(0)
        else:
            st = bs(ar, l)
            en = bs(ar, r)
            if en >= len(ar):
                an = en - st
            else:
                an = en - st + 1
                if ar[en] != r:
                    an -= 1
                if an < 0:
                    an = 0
            print(an)
