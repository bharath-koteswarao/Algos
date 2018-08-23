if __name__ == '__main__':
    for _ in range(int(input().strip())):
        d, a, m, b, x = [int(__) for __ in input().strip().split()]
        ans = (x - d) // (m * a + b)
        re = (x - d) % (m * a + b)
        ans *= (m + 1)
        if re > 0:
            ans += re // a
            re = re % a
        if re > 0:
            ans += 1
        print(ans)
