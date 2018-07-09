if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    so = sorted(arr)
    if so == arr:
        print(0)
    else:
        co = 0
        for i in range(n):
            if arr[i] != so[i]:
                co += 1
        print(1 if co == 2 else -1)
