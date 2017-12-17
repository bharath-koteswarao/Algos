if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    for _ in range(n):
        inp = input().strip().split(' ')
        name = inp[0]
        numbers = inp[2:]
        if name in dic:
            dic[name] += numbers
        else:
            dic[name] = numbers
    print(dic)
    for i in dic:
        l = dic[i]
        l2 = []
        for p in range(len(l)):
            valid = True
            for q in range(len(l)):
                a, b = l[p], l[q]
                if a.endswith(b) and p != q:
                    valid = False
            if valid:
                l2.append(a)
        dic[i] = l2
    print(dic)
