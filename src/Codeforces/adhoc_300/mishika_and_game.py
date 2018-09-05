if __name__ == '__main__':
    m, c = 0, 0
    for _ in range(int(input().strip())):
        a, b = [int(__) for __ in input().strip().split()]
        if a > b:
            m += 1
        elif a < b:
            c += 1
    if m == c:
        print("Friendship is magic!^^")
    elif m > c:
        print("Mishka")
    else:
        print("Chris")
