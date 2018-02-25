from bisect import bisect_left as bs

if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    s = input().strip()
    li = sorted(list(set(s)))
    if k > n:
        print(s + li[0] * (k - n))
    elif k == n:
        for i in range(n - 1, -1, -1):
            idx = bs(li, s[i])
            if idx != len(li) - 1:
                print(s[:i] + li[idx + 1] + li[0] * (n - i - 1))
                break
    else:
        print(s[:k - 1] + s[k])
