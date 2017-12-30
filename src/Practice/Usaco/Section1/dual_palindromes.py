"""
ID: koteswa1
LANG: PYTHON3
PROG: dualpal
"""


def getStr(n, base):
    l = []
    while n >= base:
        l.append(str(n % base))
        n //= base
    l.append(str(n))
    return ''.join(l)


def isPal(st):
    for i in range(len(st) // 2 + 1):
        if st[i] != st[len(st) - i - 1]:
            return False
    return True


if __name__ == '__main__':
    fin = open('dualpal.in', 'r')
    fout = open('dualpal.out', 'w')
    n, s = [int(i) for i in fin.readline().strip().split()]
    lis = []
    s += 1
    while n > 0:
        count = 0
        for i in range(2, 11):
            if isPal(getStr(s, i)):
                count += 1
            if count == 2:
                lis.append(s)
                n -= 1
                break
        s += 1
    ans = ""
    for i in lis:
        ans += str(i) + "\n"
    fout.write(ans)
    fout.close()
