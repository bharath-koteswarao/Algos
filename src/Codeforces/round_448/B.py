if __name__ == '__main__':
    n, x, k = [int(i) for i in input().strip().split(" ")]
    inp = [int(i) for i in input().strip().split(" ")]
    dic = {}
    for i in inp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    inp = sorted(inp)
    ans = 0
    for i in range(len(inp)):
        for j in range(i, len(inp)):
            count = 0
            a = inp[i]
            b = inp[j]
            count += (b // x - a // x)
            if a // x == a / x:
                count += 1
            if count == k:
                ans += 1
    for i in dic:
        if (dic[i] > 1 and i // x == i / x and k == 1) or k == 0:
            ans += (dic[i] * (dic[i] - 1)) // 2
    print(ans)
