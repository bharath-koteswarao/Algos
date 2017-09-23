naive_count = 0
dynamic_count = 0


def fib_naive(n):
    global naive_count
    naive_count += 1
    if n <= 2:
        return 1
    else:
        return fib_naive(n - 1) + fib_naive(n - 2)


def fib_dynamic(n, memo):
    global dynamic_count
    dynamic_count += 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_dynamic(n - 1, memo) + fib_dynamic(n - 2, memo)
        return memo[n]


def bottom_up(n, lis):
    for i in range(1, n - 1):
        lis.append(lis[i] + lis[i - 1])
    return lis


if __name__ == '__main__':
    n = int(input())
    memo = {1: 1, 2: 1}
    ans2 = fib_dynamic(n, memo)
    ans = fib_naive(n)
    ans3 = bottom_up(n, [1, 1])
    print(naive_count, dynamic_count)
    print(ans, ans2, ans3[-1])
