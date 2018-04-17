if __name__ == '__main__':
    r,c = [int(__) for __ in input().strip().split()]
    l = []
    for _ in range(r):
        l.append(list(input().strip()))
    w = 0
    for i in l:
        w += i.count('W')
    if w == 0:
        for i in l:
            print(''.join(i))
    else:
        valid = True
        for i in range(r):
            for j in range(c):
                if l[i][j] == 'S':
