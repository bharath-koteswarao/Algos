if __name__ == '__main__':
    n, m = [int(i) for i in input().strip().split()]
    a1 = [int(i) for i in input().strip().split()]
    a2 = [int(i) for i in input().strip().split()]
    arr = []
    for i in a1:
        for j in a2:
            arr.append(i * j)
    arr.sort()
    print(arr[-2])
