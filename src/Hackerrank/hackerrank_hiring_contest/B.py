if __name__ == '__main__':
    l = []
    for _ in range(int(input().strip())):
        inp = sorted(list(set(input().strip())))
        build = ""
        i, j = 0, 0
        while i < 10:
            if j < len(inp) and str(i) == inp[j]:
                build += '1'
                i += 1
                j += 1
            else:
                build += '0'
                i += 1
        l.append(build)
    dic = {}
    for i in l:
        nu = int(i, 2)
        if nu in dic:
            dic[nu] += 1
        else:
            dic[nu] = 1
    print(l)
    for i in dic:
        print(1023 - i)
