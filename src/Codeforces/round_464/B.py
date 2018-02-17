if __name__ == '__main__':
    n, k = [int(i) for i in input().strip().split()]
    arr = [int(i) for i in input().strip().split()]
    l = []
    if n == 0:
        print(1, 0)
    else:
        for i in range(len(arr)):
            l.append((i, n % arr[i]))
        l.sort(key=lambda x: x[1])
        print(l[0][0] + 1, n // arr[l[0][0]])
