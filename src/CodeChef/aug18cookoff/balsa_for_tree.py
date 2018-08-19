def getNu(n):
    re = ""
    for x in n:
        re += str(x)
    return int(re)


def brute(n):
    if str(n).count('3') > 3:
        return n + 1
    else:
        n += 1
        while str(n).count('3') < 3:
            n += 1
        return n


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        cop = n * 1
        if n < 333:
            print(333)
        elif n < 1333:
            print(1333)
        else:
            n += 1
            while str(n).count('3') < 3:
                n += 1
            print(n)
