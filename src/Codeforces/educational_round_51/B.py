if __name__ == '__main__':
    l, r = [int(__) for __ in input().strip().split()]
    print("YES")
    while l <= r:
        print(l, l + 1)
        l += 2
