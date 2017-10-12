def find_max_sum(l, i, j, limit, memo):
    if memo[i][j] != -1:
        return memo[i][j]
    else:
        if i < limit:
            memo[i][j] = max(
                l[i][j] + find_max_sum(l, i + 1, j, limit, memo),
                l[i][j] + find_max_sum(l, i + 1, j + 1, limit, memo)
            )
            return memo[i][j]
        else:
            memo[i][j] = 0
            return memo[i][j]
    pass


if __name__ == '__main__':
    tc = int(input().strip(" "))
    for tc_i in range(tc):
        size = int(input().strip())
        l = [[] for i in range(size)]
        for i in range(size):
            l[i] = [int(i) for i in input().strip().split(" ")]
        memo = [[-1 for i in range(size + 1)] for i in range(size + 1)]
        ans = find_max_sum(l, 0, 0, size, memo)
        print(ans)
