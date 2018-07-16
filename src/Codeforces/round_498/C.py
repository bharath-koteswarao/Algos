if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    p = [arr[0]]
    for i in range(1, n):
        p.append(p[i - 1] + arr[i])
    prev = [arr[-1]]
    arr = arr[::-1]
    for i in range(1, n):
        prev.append(prev[i - 1] + arr[i])
    prev = prev[::-1]
    dic = {}
    for i in range(n):
        dic[p[i]] = i
    ans = 0
    for i in range(n):
        if prev[i] in dic and i > dic[prev[i]]:
            ans = max(ans, prev[i])
    print(ans)
