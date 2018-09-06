memo = [-1 for i in range(10 ** 6 + 1)]


def f(x):
    pro = 1
    while x != 0:
        re = x % 10
        pro *= re if re != 0 else 1
        x //= 10
    return pro


def g(x):
    global memo
    if memo[x - 1] != -1:
        # print("prevented " + str(x))
        return memo[x - 1]
    else:
        if x < 10:
            return x
        else:
            memo[x - 1] = g(f(x))
            return memo[x - 1]


if __name__ == '__main__':
    pre = [
        [0 for j in range(10 ** 6)] for i in range(9)
    ]
    for i in range(9):
        pre[i - 1][i - 1] = 1
    for i in range(2, 10 ** 6 + 1):
        val = g(i)
        for j in range(9):
            if j == val - 1:
                pre[j][i - 1] = pre[j][i - 2] + 1
            else:
                pre[j][i - 1] = pre[j][i - 2]
    q = int(input().strip())
    for _ in range(q):
        l, r, k = [int(__) for __ in input().strip().split()]
        l -= 1
        r -= 1
        if l == 0:
            print(pre[k - 1][r])
        else:
            print(pre[k - 1][r] - pre[k - 1][l - 1])
