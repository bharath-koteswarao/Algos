if __name__ == '__main__':
    tc = int(input().strip())
    test_cases = []
    for i_tc in range(tc):
        test_cases.append(int(input().strip()))
    biggest = max(test_cases)
    dic = {}
    for n in range(1, biggest + 1):
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
    calculated = {}
    for test_case in test_cases:
        total = 0
        for i in range(1, test_case + 1):
            temp = dic[i]
            if temp in dic and dic[temp] == i and i != temp:
                total += temp
        print(total)
        calculated[test_case] = total
