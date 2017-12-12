if __name__ == '__main__':
    tc = int(input().strip())
    p, q = 0, 0
    for _ in range(tc):
        a, b = [int(i) for i in input().strip().split(" ")]
        if a > 0:
            p += 1
        else:
            q += 1
    if p == 0 or q == 0:
        print("Yes")
    elif p == 1 or q == 1:
        print("Yes")
    else:
        print("No")
