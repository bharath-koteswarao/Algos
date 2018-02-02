"""
6
1 2 5 3 4 6
01110
"""
if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    l = list(input().strip())
    l.append('1')
    dic = {}
    ind = 0
    for i in arr:
        dic[i] = ind
        ind += 1
    ones = []
    c = 0
    for i in l:
        if i == '1':
            c += 1
        ones.append(c)
    so = sorted(arr)
    possible = True
    check = {}
    for ii in range(n):
        if so[ii] != arr[ii]:
            idx = dic[so[ii]]
            lis = l[min(idx, ii): max(idx, ii)]
            if ii == 0:
                co = ones[idx]
            elif idx == 0:
                co = ones[ii]
            else:
                co = abs(ones[max(idx, ii)] - ones[min(idx, ii) - 1])
            if co == abs(idx - ii) + 1:
                pass
            elif co == abs(idx - ii) and l[max(idx,ii)] == '0':
                pass
            else:
                possible = False
        if not possible:
            break
    print("YES" if possible else "NO")
