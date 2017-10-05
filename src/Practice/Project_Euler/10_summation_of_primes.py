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
    n = 3
    while n <= largest:
        if is_prime(n):
            primes.append(n)
        n += 2
    answers = {}
    total = 0
    for i in primes:
        total += i
        answers[i] = total
    for i in test_cases:
        if i in answers:
            print(answers[i])
        else:
            while i not in answers:
                i -= 1
            print(answers[i])
