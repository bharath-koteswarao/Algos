from pprint import pprint as pp
def max_factor(n):
    m = int(n ** 0.5)
    while n % m is not 0 and m >= 1:
        m -= 1
    if m == 1:
        return n - 1
    return int(max(m, n / m))


def min_moves(n, memo):
    if n in memo:
        return memo[n]
    if n is 0:
        return 0
    if n < 0:
        return float("inf")
    factor = max_factor(n)
    if factor is n - 1:
        memo[n] = min_moves(n - 1, memo) + 1
        return memo[n]
    else:
        left = min_moves(n - 1, memo) + 1
        right = min_moves(max_factor(n), memo) + 1
        memo[n] = min(left, right)
        return memo[n]


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n = int(input())
        memo = {}
        ans = min_moves(n, memo)
        print(ans)
        # pp(memo)
