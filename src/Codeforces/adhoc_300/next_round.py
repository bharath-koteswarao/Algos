if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]

    k = arr[k - 1]
    ans = 0
    for i in arr:
        if i >= k and i != 0:
            ans += 1
    print(ans)
