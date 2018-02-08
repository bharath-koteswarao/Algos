if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = [int(__) for __ in input().strip().split()]
        c, d, s = [int(__) for __ in input().strip().split()]
        delay = (c - 1) * arr[0]
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                delay += (c - 1) * (arr[i] - arr[i - 1])
        print(delay)
