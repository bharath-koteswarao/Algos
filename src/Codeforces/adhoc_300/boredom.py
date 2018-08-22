from collections import Counter

if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ma = max(arr)
    dp = [0 for i in range(ma + 1)]
    cnt = Counter(arr)
    for i in range(1, ma + 1):
        prev = 0 if i == 1 else dp[i - 2]
        dp[i] = max(i * cnt[i] + prev, dp[i - 1])
    print(max(dp))
