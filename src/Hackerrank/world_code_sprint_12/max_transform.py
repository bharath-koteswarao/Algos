if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    l = []
    for k in range(len(arr)):
        for i in range(len(arr) - k):
            j = i + k
            print(max(arr[i:j + 1]))
    print(l)
