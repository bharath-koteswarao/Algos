def getSum(i):
    ret = 0
    while i != 0:
        ret += i % 10
        i //= 10
    return ret


if __name__ == '__main__':
    n = int(input().strip())
    l = [19]
    i = 20
    while len(l) != n:
        su = getSum(i)
        if su == 10:
            l.append(i)
        i += 9
    print(l[-1])
