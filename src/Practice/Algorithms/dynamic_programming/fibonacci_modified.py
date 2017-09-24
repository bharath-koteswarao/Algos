def bottom_up(n, lis):
    for i in range(1, n - 1):
        lis.append(lis[i] ** 2 + lis[i - 1])
    return lis


if __name__ == '__main__':
    (t1, t2, n) = [int(i) for i in input().split(" ")]
    ans3 = bottom_up(n, [t1, t2])
    print(ans3[n-1])
