if __name__ == '__main__':
    ans = 0
    for _ in range(int(input().strip())):
        a, b = [int(__) for __ in input().strip().split()]
        ans += 1 if b - a >= 2 else 0
    print(ans)