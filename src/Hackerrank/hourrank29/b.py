from math import gcd


def prod(arr):
    p = 1
    for j in arr:
        p *= j
    return p


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        ans = 0
        mod = 1000000007
        arr = [int(__) for __ in input().strip().split()]
        for i in range(1, 2 ** (n - 1)):
            s1, s2 = [], []
            bi = bin(i)[2:]
            bi = '0' * (n - len(bi)) + bi
            for j in range(len(bi)):
                if bi[j] == '1':
                    s1.append(arr[j])
                else:
                    s2.append(arr[j])
            if gcd(prod(s1), prod(s2)) == 1:
                ans += 2 % mod
        print(ans)
