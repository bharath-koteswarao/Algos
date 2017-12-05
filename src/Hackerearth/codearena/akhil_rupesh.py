if __name__ == '__main__':
    n = int(input().strip())
    ar = [int(i) for i in input().strip().split(" ")]
    dic = {}
    for i in range(len(ar)):
        if ar[i] in dic:
            dic[ar[i]].append(i)
        else:
            dic[ar[i]] = [i]
    s = 0
    for i in dic:
        l = len(dic[i])
        s += (l * (l - 1)) // 2
    print(s)
