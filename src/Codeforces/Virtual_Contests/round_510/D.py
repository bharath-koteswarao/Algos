from bisect import bisect_left as bs

if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    pre = [arr[0]]
    for i in range(1, len(arr)):
        pre.append(arr[i] + pre[-1])
    ans = 0
    for el in arr:
        if el < k:
            ans += 1
    for el in pre:
        if el < k:
            ans += 1
    for i in range(len(pre)):
        if i + 2 < len(pre):
            find = sorted(pre[i + 2:])
            se = pre[i] + k - 1 - 0.001
            idx = bs(find, se)
            if arr[idx] <= k:
                ans += idx + 1
            else:
                if idx > 0:
                    ans += idx
    print(ans)
