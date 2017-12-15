def find_lpf(n):
    las = 0
    while n % 2 == 0 and n != 0:
        n = n // 2
        las = 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0 and n != 0:
            n = n // i
            las = i
    if n > 2:
        las = n
    return las


def find_all(n, lpf):
    if n not in lpf:
        lpf[n] = find_lpf(n)
        find_all(n // lpf[n], lpf)
    pass


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    lpf = {1: 1}
    for i in arr:
        find_all(i, lpf)
    ans = 0
    for i in arr:
        temp, su = 1, 1
        while i != 1:
            temp *= lpf[i]
            i //= lpf[i]
            su += temp
        ans += su
    print(ans)
