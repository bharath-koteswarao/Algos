if __name__ == '__main__':
    tc = int(input())
    for tc_i in range(tc):
        n = int(input().strip())
        primes = {1: [1]}
        for i in range(n + 1):
            count = 0
            while i % 2 == 0 and i != 0:
                count += 1
                i >>= 1
            if 2 not in primes:
                primes[2] = [count]
            else:
                primes[2].append(count)
            for j in range(3, int(i ** 0.5) + 1, 2):
                count = 0
                while i % j == 0:
                    i //= j
                    count += 1
                if count > 0 and j not in primes:
                    primes[j] = [count]
                elif count > 0:
                    primes[j].append(count)
            if i > 2:
                if i not in primes:
                    primes[i] = [1]
                else:
                    primes[i].append(1)
        answer = 1
        for i in primes:
            maximum = max(primes[i])
            answer *= i ** maximum
        print(answer)
