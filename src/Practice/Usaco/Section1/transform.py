"""
ID: koteswa1
LANG: PYTHON3
PROG: transform
"""


def rotate(inp):
    tempMat = [[0 for i in range(n)] for j in range(n)]
    p, q = 0, 0
    for i in range(n):
        q = 0
        for j in range(n - 1, -1, -1):
            tempMat[p][q] = inp[j][i]
            q += 1
        p += 1
    inp[:] = tempMat[:]
    return tempMat


def reflection(tempInp):
    for i in range(len(tempInp)):
        tempInp[i] = tempInp[i][::-1]
    inp[:] = tempInp[:]
    return tempInp


if __name__ == '__main__':
    fin = open('transform.in', 'r')
    fout = open('transform.out', 'w')
    n = int(fin.readline().strip())
    inp, op = [], []
    for _ in range(n):
        inp.append(list(fin.readline().strip()))
    for _ in range(n):
        op.append(list(fin.readline().strip()))
    tempInp = inp[:]
    ans = ""
    found = False
    if inp == op:
        ans = str(6)
        found = True
    else:
        for i in range(1, 4):
            rotate(tempInp)
            if tempInp == op:
                ans = str(i)
                found = True
                break
    if not found:
        inp = reflection(inp)
        if inp == op:
            ans = str(4)
            found = True
        else:
            for i in range(3):
                rotate(inp)
                if inp == op:
                    ans = str(5)
                    found = True
                    break
    if not found:
        ans = str(7)
    fout.write(ans + "\n")
    fout.close()
