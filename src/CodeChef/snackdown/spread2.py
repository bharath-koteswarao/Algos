if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = [int(__) for __ in input().strip().split()]
        pre = [arr[0]]
        for i in range(1, len(arr)):
            pre.append(pre[-1] + arr[i])
        ans = 0
        i = 0
        while i < n - 1:
            ans += 1
            i += pre[i]
        print(ans)

"""
1
17
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 

"""
