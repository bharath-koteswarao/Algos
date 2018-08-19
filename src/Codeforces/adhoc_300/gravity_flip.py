if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    arr.sort()
    for x in arr:
        print(x, end=" ")
