if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n = int(input().strip())
        dic = {}
        count = 0
        while n % 2 == 0 and n != 0:
            n //= 2
            count += 1
        if count > 0:
            dic[2] = count
        for i in range(3, int(n ** 0.5) + 1, 2):
            count = 0
            while n % i == 0 and n > 0:
                n //= i
                count += 1
            if count > 0:
                dic[i] = count
        if n > 2:
            dic[n] = 1
        mul = 1
        for i in dic:
            mul *= (dic[i] + 1)
        print(mul)
