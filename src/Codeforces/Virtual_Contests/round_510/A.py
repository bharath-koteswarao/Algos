from math import ceil

if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    l = []
    for _ in range(n):
        l.append(int(input().strip()))
    l.sort()
    ma = l[-1] + m
    mi = ceil((sum(l) + m) // n)
    if (sum(l) + m) % n > 0:
        mi += 1
    print(mi, ma)
