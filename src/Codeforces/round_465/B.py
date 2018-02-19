if __name__ == '__main__':
    n = int(input().strip())
    arr = list(input().strip())
    cur = [0, 0]
    cost = 0
    if arr[0] == 'U':
        cur[1] += 1
    else:
        cur[0] += 1
    lowar = cur[0] > cur[1]
    for i in range(1, len(arr)):
        if arr[i] == 'U':
            cur[1] += 1
        else:
            cur[0] += 1
        if lowar:
            if cur[0] < cur[1]:
                cost += 1
                lowar = False
        else:
            if cur[0] > cur[1]:
                cost += 1
                lowar = True
    print(cost)
