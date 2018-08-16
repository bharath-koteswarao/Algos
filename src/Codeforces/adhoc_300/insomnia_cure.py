if __name__ == '__main__':
    k = int(input().strip())
    l = int(input().strip())
    m = int(input().strip())
    n = int(input().strip())
    d = int(input().strip())
    arr = [False for i in range(d)]
    for i in range(k - 1, d, k):
        arr[i] = True
    for i in range(l - 1, d, l):
        arr[i] = True
    for i in range(m - 1, d, m):
        arr[i] = True
    for i in range(n - 1, d, n):
        arr[i] = True
    print(arr.count(True))
