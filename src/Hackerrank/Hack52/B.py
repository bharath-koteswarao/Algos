if __name__ == '__main__':
    n, k, x = [int(i) for i in input().strip().split(" ")]
    ans = 0
    count = 0
    for i in range(n - 2, -1, -1):
        ans += ((-1) ** count) * ((k - 1) ** i)
        count += 1
    print(ans % 1000000007)
