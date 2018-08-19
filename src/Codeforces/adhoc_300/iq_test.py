if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) % 2 for __ in input().strip().split()]
    z, o = arr.count(0), arr.count(1)
    if z > o:
        print(arr.index(1) + 1)
    else:
        print(arr.index(0) + 1)
