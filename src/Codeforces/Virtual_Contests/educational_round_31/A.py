if __name__ == '__main__':
    n, t = [int(i) for i in input().strip().split(" ")]
    arr = [int(i) for i in input().strip().split(" ")]
    day = 86400
    count, i = 1, 0
    while True:
        diff = 86400 - arr[i]
        t -= diff
        if t <= 0:
            break
        else:
            i += 1
            count += 1
    print(count)
