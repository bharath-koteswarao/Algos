if __name__ == '__main__':
    fact = {'1': 1,
            '2': 2,
            '3': 6,
            '4': 24,
            '5': 120,
            '6': 720,
            '7': 5040,
            '8': 40320,
            '9': 362880,
            '0': 1}
    n = int(input().strip())
    answer = 0
    for i in range(10, n + 1):
        nums = list(str(i))
        total = 0
        for j in nums:
            total += fact[j]
        if total % i == 0:
            answer += i
    print(answer)
