if __name__ == '__main__':
    n, q = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    le = len(bin(max(arr))) - 2
    for i in range(len(arr)):
        arr[i] = bin(arr[i])[2:].zfill(le)
    # print(arr)
    dic = {}
    for i in range(le):
        x = arr[0][i]
        pre = [1 if arr[0][i] == '1' else 0]
        for j in range(1, n):
            if arr[j][i] == '1':
                pre.append(pre[j - 1] + 1)
            else:
                pre.append(pre[j - 1])
        dic[i] = pre
    for _ in range(q):
        ans = ['0' for i in range(le)]
        l, r = [int(__) for __ in input().strip().split()]
        l, r = l - 1, r - 1
        for i in range(le):
            ones = 0
            if l == 0:
                ones = dic[i][r]
            else:
                ones = dic[i][r] - dic[i][l - 1]
            zros = r - l + 1 - ones
            if zros > ones:
                ans[i] = '1'
            else:
                ans[i] = '0'
        print(int(('1' * (31 - le)) + ''.join(ans), 2))
