def getPf(n):
    dic = {}
    count = 0
    while n % 2 == 0 and n > 0:
        count += 1
        n //= 2
    if count > 0:
        dic[2] = count
    for i in range(3,int(n ** 0.5) + 1):
        count = 0
        while n % i == 0 and n > 0:
            count += 1
            n //= i
        if count > 0:
            dic[i] = count
    if n > 2:
        dic[n] = 1
    return dic

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        ans = 0
        for i in range(1,n + 1):
            dic = getPf(i)
            res = 1
            for j in dic:
                res *= (j ** dic[j] - j ** (dic[j] - 1))
            if (i - res) % 2 == 1:
                ans += 1
        print(ans)