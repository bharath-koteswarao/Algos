if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    dic = {arr[0]: 1}
    ic = [0 for i in range(n)]
    isu = [0 for i in range(n)]
    pre = [arr[0]]
    for i in range(1, n):
        pre.append(pre[i - 1] + arr[i])
    for i in range(1, n):
        ici, isi = 0, 0
        if arr[i] in dic:
            ici += dic[arr[i]]
            isi += arr[i] * dic[arr[i]]
        if arr[i] - 1 in dic:
            ici += dic[arr[i] - 1]
            isi += (arr[i] - 1) * dic[arr[i] - 1]
        if arr[i] + 1 in dic:
            ici += dic[arr[i] + 1]
            isi += (arr[i] + 1) * dic[arr[i] + 1]
        ic[i], isu[i] = ici, isi
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    ans = 0
    for i in range(1, n):
        ans += (arr[i] * i) - pre[i - 1] - ic[i] * arr[i] + isu[i]
    print(ans)
