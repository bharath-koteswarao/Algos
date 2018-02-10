if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(i) for i in input().strip().split()]
        print(((n * (n + 1) * (n + 2)) // 6) % k)
