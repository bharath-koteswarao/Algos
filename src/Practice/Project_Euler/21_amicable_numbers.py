from pprint import pprint as pp

if __name__ == '__main__':
    tc = int(input().strip())
    for i_tc in range(tc):
        p = int(input().strip())
        dic = {}
        for n in range(p + 1):
            temp_n = n
            primes = {}
            count = 0
            while n % 2 == 0 and n != 0:
                n //= 2
                count += 1
            if count > 0:
                primes[2] = count
            for i in range(3, int(n ** 0.5) + 1, 2):
                count = 0
                while n % i == 0:
                    n //= i
                    count += 1
                if count > 0:
                    primes[i] = count
            if n > 2:
                if n in primes:
                    primes[n] += 1
                else:
                    primes[n] = 1
            mul = 1
            for i in primes:
                mul *= (i ** (primes[i] + 1) - 1) // (i - 1)
            dic[temp_n] = mul - temp_n
        total = 0
        # pp(dic)
        for i in dic:
            temp = dic[i]
            if temp in dic and dic[temp] == i and i != temp:
                total += i
                # print(i)
        print(total-1)
