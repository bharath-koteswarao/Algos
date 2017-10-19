def find(str1, str2, i, j, memo):
    if memo[i][j] != -1:
        return memo[i][j]
    elif i >= len(str1) or j >= len(str2):
        return 0
    elif str1[i] == str2[j]:
        memo[i][j] = 1 + find(str1, str2, i + 1, j + 1, memo)
        return memo[i][j]
    else:
        memo[i][j] = max(
            find(str1, str2, i + 1, j, memo),
            find(str1, str2, i, j + 1, memo)
        )
        return memo[i][j]


if __name__ == '__main__':
    str1 = input().strip()
    str2 = input().strip()
    memo = [[-1 for i in range(max(len(str1), len(str2)) + 1)] for j in range(max(len(str1), len(str2)) + 1)]
    ans = find(str1, str2, 0, 0, memo)
    print(ans)
