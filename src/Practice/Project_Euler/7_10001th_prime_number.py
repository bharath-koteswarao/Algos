def is_prime(n):
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    tc = int(input().strip())
    test_cases = []
    largest = 0
    for i_tc in range(tc):
        test_cases.append(int(input().strip()))
        largest = max(largest, test_cases[i_tc])
    primes = [2]
    num = 3
    while largest - 1 > 0:
        if is_prime(num):
            primes.append(num)
            largest -= 1
        num += 2
    for i in test_cases:
        print(primes[i - 1])
