def c(n, r):
    mod = 1000000007
    dp = [[0 for x in range(r + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, r) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] % mod + dp[i - 1][j] % mod) % mod
    return dp[n][r] % mod
