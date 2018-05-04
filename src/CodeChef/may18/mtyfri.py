if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        motu, tomu = [], []
        s1, s2 = 0, 0
        for i in range(len(arr)):
            if i % 2 == 0:
                motu.append(arr[i])
                s1 += arr[i]
            else:
                tomu.append(arr[i])
                s2 += arr[i]
        motu.sort(reverse=True)
        tomu.sort()
        if s2 > s1:
            print("YES")
        else:
            i, j = 0, 0
            while i < len(motu) and j < len(tomu) and k > 0 and s1 >= s2:
                if motu[i] > tomu[j]:
                    dif = abs(motu[i] - tomu[j])
                    s1 -= dif
                    s2 += dif
                    i += 1
                    j += 1
                    k -= 1
                else:
                    break
            print("YES" if s2 > s1 else "NO")
