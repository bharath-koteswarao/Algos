if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    co = arr[:]
    arr.sort()
    arr = arr[::-1]
    ans = 0
    dic = {}
    for i in range(k):
        ans += arr[i]
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    print(ans)
    count = 1
    for i in range(n):
        if co[i] in dic and dic[co[i]] >= 1 and k > 1:
            print(count, end=" ")
            dic[co[i]] -= 1
            k -= 1
            count = 0
        elif i == n - 1:
            print(count)
        count += 1
