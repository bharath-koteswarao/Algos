if __name__ == '__main__':
    a, b = [int(__) for __ in input().strip().split()]
    ans = 0
    while a <= b:
        ans += 1
        a *= 3
        b <<= 1
    print(ans)
