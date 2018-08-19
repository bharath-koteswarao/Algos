if __name__ == '__main__':
    n = int(input().strip())
    arr = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    if n <= 5:
        print(arr[n - 1])
    else:
        su = 5
        i = 1
        while (5 * (2 ** i)) + su < n:
            su += 5 * (2 ** i)
            i += 1
        count = 2 ** i
        # print(n - su, count)
        cur = count
        idx = 0
        while cur < n - su:
            cur += count
            idx += 1
        print(arr[idx])
