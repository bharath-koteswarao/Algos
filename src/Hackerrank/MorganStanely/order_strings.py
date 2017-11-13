"""
3
92 022
82 002
1 022
2 true lexicographic

3
1 002
2 002
3 002
2 false numeric
"""
if __name__ == '__main__':
    n = int(input().strip())
    l = [[] for i in range(n)]
    for i in range(n):
        l[i] = input().strip().split(" ")
    key, rev, order = input().strip().split(" ")
    key = int(key)
    dic = {}
    count = 1
    for i in range(n):
        if l[i][key - 1] not in dic:
            dic[l[i][key - 1]] = l[i]
        else:
            dic[l[i][key - 1] + '0' * count] = l[i]
            count += 1
    if order == "lexicographic":
        arr = sorted(list(dic.keys()), reverse=rev == "true")
        for i in arr:
            lis = dic[i]
            for j in lis:
                print(j, end=" ")
            print()
    else:
        conv = {}
        nex = 0
        for i in dic:
            if int(i) not in conv:
                conv[int(i)] = i
            else:
                replace = int(str(int(i)) + str(nex))
                nex += 1
                conv[replace] = i
        keys = list(conv.keys())
        keys = sorted(keys, reverse=rev == "true")
        for i in keys:
            con = conv[i]
            lis = dic[con]
            for j in lis:
                print(j, end=" ")
            print()
