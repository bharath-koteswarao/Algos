def getCount(arr, start, end):
    if start == 0:
        return arr[end]
    else:
        return arr[end] - arr[start - 1]
if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        su = [arr[0]]
        for i in range(1, len(arr)):
            su.append(arr[i] + su[i - 1])
        ans = 0
        for i in range(len(arr) - k + 1):
            ans = max(ans, getCount(su, i, i + k - 1))
        print(ans)