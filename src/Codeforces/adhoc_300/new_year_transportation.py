if __name__ == '__main__':
    n, t = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    cur = 0
    while cur != t - 1 and cur < t - 1:
        cur = arr[cur] + cur
    print("YES" if cur == t - 1 else "NO")
