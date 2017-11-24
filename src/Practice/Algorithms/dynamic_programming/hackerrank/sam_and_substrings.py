if __name__ == '__main__':
    inp = list(input().strip())[::-1]
    s = 0
    mod = 1000000007
    l = len(inp)
    ones = 1
    j = 1
    for i in inp:
        s += (int(i) * ones * l) % mod
        l -= 1
        ones = (ones * 10 + 1) % mod
    print(s % mod)
