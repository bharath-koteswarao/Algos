if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    if n == 1:
        print(0)
    else:
        arr.sort()
        ans = arr[-1] - arr[0] + 1 - len(arr)
        print(ans)