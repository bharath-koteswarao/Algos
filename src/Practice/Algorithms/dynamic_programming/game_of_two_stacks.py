def find_max_score(arr1, arr2, limit, memo, i, j):
    if len(arr1) > 0 and len(arr2) > 0 and limit > 0:
        if limit - arr1[0] >= 0 and limit - arr2[0] >= 0:
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(
                    1 + find_max_score(arr1[1:], arr2, limit - arr1[0], memo, i + 1, j),
                    1 + find_max_score(arr1, arr2[1:], limit - arr2[0], memo, i, j + 1)
                )
                return memo[(i, j)]
        elif limit - arr1[0] >= 0:
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                memo[(i, j)] = 1 + find_max_score(arr1[1:], arr2, limit - arr1[0], memo, i + 1, j)
                return memo[(i, j)]
        elif limit - arr2[0] >= 0:
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                memo[(i, j)] = 1 + find_max_score(arr1, arr2[1:], limit - arr2[0], memo, i, j + 1)
                return memo[(i, j)]
        else:
            return 0

    else:
        return 0
    pass


if __name__ == '__main__':
    tc = int(input().strip())
    for i_tc in range(tc):
        n1, n2, limit = [int(i) for i in input().strip().split(" ")]
        arr1 = [int(i) for i in input().strip().split(" ")]
        arr2 = [int(i) for i in input().strip().split(" ")]
        memo = {}
        ans = find_max_score(arr1, arr2, limit, memo, 0, 0)
        print(ans)
