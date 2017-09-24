if __name__ == '__main__':
    (n, p, q, r) = [int(i) for i in input().split(" ")]
    lis = [int(i) for i in input().split(" ")]
    lis_max = max(lis)
    lis_min = min(lis)
    first = [p, q, r]
    first = sorted(first)
    lis = sorted(lis)
    ans = 0
    for j in range(3):
        if first[j] >= 0:
            ans += first[j] * lis_max
        else:
            ans += first[j] * lis_min

    print(ans)
