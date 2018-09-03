if __name__ == '__main__':
    n = int(input().strip())
    po, ans = 0, 0
    arr = [int(__) for __ in input().strip().split()]
    for i in range(n):
        if arr[i] == -1:
            if po > 0:
                po -= 1
            else:
                ans += 1
        else:
            po += arr[i]
    print(ans)