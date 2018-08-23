if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    co = 0
    for i in arr:
        if 5 - i >= k:
            co += 1
    print(co // 3)