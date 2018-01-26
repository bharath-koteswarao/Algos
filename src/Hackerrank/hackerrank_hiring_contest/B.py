if __name__ == '__main__':
    l = []
    for _ in range(int(input().strip())):
        inp = sorted(list(set(input().strip())))
        build = []
        i, j = 0, 0
        while i < 10:
            if j < len(inp) and str(i) == inp[j]:
                build.append('1')
                i += 1
                j += 1
            else:
                build.append('0')
                i += 1
        l.append(''.join(build))
    c = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            # print(l[i], l[j], int(l[i], 2) | int(l[j], 2))
            if int(l[i], 2) | int(l[j], 2) == 1023:
                c += 1
    print(c)
