def f(k, n):
    su = 0
    i = 1
    while i <= n:
        su += i
        i *= k
    return su


if __name__ == '__main__':
    ans = 0
    for i in range(1, 6):
        p = f(2, i)
        print(p)
    print(ans)
