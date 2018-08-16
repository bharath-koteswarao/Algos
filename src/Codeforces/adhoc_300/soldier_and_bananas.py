if __name__ == '__main__':
    k, n, w = [int(__) for __ in input().strip().split()]
    req = (w * (w + 1)) // 2
    req *= k
    if req - n <= 0:
        print(0)
    else:
        print(req - n)