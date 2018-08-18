if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    arr = [int(__) for __ in input().strip().split()]
    for i in range(1, n + 1):
        dic[arr[i - 1]] = i
    for i in range(1, n + 1):
        print(dic[i], end=" ")
