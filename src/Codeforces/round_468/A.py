from math import ceil

if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    dif = abs(n - m)
    if dif == 1:
        print(1)
    elif dif == 2:
        print(2)
    elif dif % 2 == 1:
        mid = ceil(max(m, n) - min(m, n))
        print(dif + 2 * ((dif * (dif - 1)) // 2))
    else:
        mid = (max(m, n) - min(m, n)) // 2
        print(dif * 2 + 2 * ((dif * (dif - 1)) // 2))
