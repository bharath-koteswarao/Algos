if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n, k = [int(i) for i in input().strip().split(" ")]
        arr = [int(i) for i in input().strip().split(" ")]
        biggest = max(arr)
        l = []
        for i in range(k):
            l.append(biggest + 1)
            biggest += 1
        arr = arr + l
        arr = sorted(arr)
        print(arr[(n + k) // 2])
