if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(i) for i in input().strip().split()]
        arr = [int(i) for i in input().strip().split()]
        for i in range(len(arr)):
            arr[i] -= 1
        l = [10 ** 10 for i in range(n)]
        for i in arr:
            for j in range(len(l)):
                l[j] = min(l[j], abs(j - i) + 1)
        print(max(l))
