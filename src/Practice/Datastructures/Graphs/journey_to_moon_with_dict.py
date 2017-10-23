if __name__ == '__main__':
    n, p = [int(i) for i in input().strip().split(" ")]
    dic = {}
    for i in range(n):
        dic[i] = []
    for i in range(p):
        a, b = [int(i) for i in input().strip().split(" ")]
        dic[a].append(b)
        dic[b].append(a)
    print(dic)
    temp = dic
