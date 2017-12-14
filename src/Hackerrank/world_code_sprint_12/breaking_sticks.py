def pf(n):
    dic = {}
    count = 0
    while n % 2 == 0 and n is not 0:
        n >>= 1
        count += 1
    if count > 0:
        dic[count] = count
    for i in range(3, int(n ** 0.5) + 1, 2):
        count = 0
        while n % i == 0 and n > 0:
            n = n // i
            count += 1
        dic[i] = count
    if n > 2:
        dic[n] = 1
    return dic


if __name__ == '__main__':
    n = int(input().strip())
    l = [int(i) for i in input().strip().split(" ")]
    ans = 0
    for i in l:
        primes = pf(i)
        if i in primes:
            ans += i + 1
        else:
            md = 0
            d = []
            if i % 2 == 0:
                for p in range(2, int(i ** 0.5) + 1):
                    if i % p == 0:
                        d.append(p)
                print(d)
            else:
                for p in range(3, int(i ** 0.5) + 1, 2):
                    if i % p == 0:
                        d.append(p)
    print(ans)
