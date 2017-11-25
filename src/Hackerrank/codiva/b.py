"""
3
1 1 2
1 3 2
3
1
1
2
2
1 2
2
1
3
1
"""
if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    inp1 = [int(i) for i in input().strip().split(" ")]
    inp2 = [int(i) for i in input().strip().split(" ")]
    for i in range(len(inp1)):
        if inp1[i] not in dic:
            dic[inp1[i]] = [inp2[i]]
        else:
            dic[inp1[i]].append(inp2[i])
    q = int(input().strip())
    for _ in range(q):
        d = int(input().strip())
        brands = [int(i) for i in input().strip().split(" ")]
        ch = int(input().strip())
        lis = []
        for i in brands:
            if i in dic:
                lis += dic[i]
        if len(lis) == 0:
            print(-1)
        else:
            lis = sorted(lis)
            if ch - 1 > len(lis) - 1:
                print(lis[0])
            else:
                print(lis[ch - 1])
