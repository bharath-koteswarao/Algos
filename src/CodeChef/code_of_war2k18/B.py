if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        lis = [int(i) for i in input().strip().split()]
        lis.sort()
        if n == 1:
            print(lis[0])
        elif n == 2:
            print(sum(lis))
        else:
            pre = [lis[0]]
            for i in range(1, n):
                pre.append(pre[i - 1] + lis[i])
            print(sum(pre[1:]))
