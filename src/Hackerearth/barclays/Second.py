if __name__ == '__main__':
    n = int(input().strip())
    a = [int(i) for i in input().strip().split()]
    b = [int(i) for i in input().strip().split()]
    ans1 = 0
    for i in a:
        ans1 = ans1 | i
    ans2 = 0
    for i in b:
        ans2 = ans2 | i
    r1 = sum(a) - ans1
    r2 = sum(b) - ans2
    if r1 > r2:
        print(1, abs(r1 - r2))
    else:
        print(2, abs(r1 - r2))
