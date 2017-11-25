if __name__ == '__main__':
    n, q = [int(i) for i in input().strip().split(" ")]
    lis = [0 for i in range(n)]
    dic = {}
    for i in range(n):
        dic[i] = 0
    for _ in range(q):
        inp = [int(i) for i in input().strip().split(" ")]
        if inp[0] == 1:
            l, r, val = inp[1], inp[2], inp[3]
            for i in range(l - 1, r):
                lis[i] ^= val

