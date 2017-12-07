if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    arr = sorted(arr)[::-1]
    for i in range(1,len(arr)+1):
        arr[i-1] += i
    print(max(arr))