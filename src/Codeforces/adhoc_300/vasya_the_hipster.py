if __name__ == '__main__':
    a, b = [int(__) for __ in input().strip().split()]
    ans = min(a, b)
    a = max(0, a - ans)
    b = max(0, b - ans)
    print(ans, a // 2 + b // 2)