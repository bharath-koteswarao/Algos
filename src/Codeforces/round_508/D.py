if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    if n == 1:
        print(arr[0])
    else:
        ne = 0
        for i in arr:
            if i < 0:
                ne += 1
        if ne == len(arr):
            arr = [abs(i) for i in arr]
            print(sum(arr) - 2 * min(arr))
        else:
            mi = min(arr)
            arr = [abs(i) for i in arr]
            if mi < 0:
                print(sum(arr))
            else:
                print(sum(arr) - 2 * mi)
