from itertools import combinations as comb


def prod(tup):
    pro = 1
    for p in tup:
        pro *= p
    return pro


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, q = [int(i) for i in input().strip().split()]
        arr = [int(i) for i in input().strip().split()]
        ans = 0
        for i in range(1, q + 1):
            combs = comb(arr, i)
            for a in combs:
                if i % 2 == 1:
                    ans += n // prod(a)
                else:
                    ans -= n // prod(a)
        print(ans)
