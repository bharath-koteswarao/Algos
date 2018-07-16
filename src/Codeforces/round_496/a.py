if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    l = []
    for i in range(len(arr)):
        if arr[i] == 1:
            l.append(i)
    print(len(l))
    print(l)
