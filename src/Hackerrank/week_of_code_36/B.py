if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    ma = arr.count(1)
    mi = 0
    for i in range(len(arr) - 1):
        if arr[i] == 1:
            if arr[i + 1] == 1:
                arr[i + 1] = 0
            mi += 1
    if arr[-1] == 1:
        mi += 1
    print(mi, ma)
