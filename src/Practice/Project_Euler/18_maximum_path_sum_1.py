def find_max_sum(l, i, j, limit):
    if i < limit:
        return max(
            l[i][j] + find_max_sum(l, i + 1, j, limit),
            l[i][j] + find_max_sum(l, i + 1, j + 1, limit)
        )
    else:
        return 0
    pass


if __name__ == '__main__':
    tc = int(input().strip(" "))
    for tc_i in range(tc):
        size = int(input().strip())
        l = [[] for i in range(size)]
        for i in range(size):
            l[i] = [int(i) for i in input().strip().split(" ")]
        ans = find_max_sum(l, 0, 0, size)
        print(ans)
