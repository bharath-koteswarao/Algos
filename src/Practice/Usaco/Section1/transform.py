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
    tempInp = tempInp[::-1]
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
    if inp == op:
        ans = str(6)
    elif rotate(tempInp) == op:
        ans = str(1)
    elif rotate(tempInp) == op:
        ans = str(2)
    elif rotate(tempInp) == op:
        ans = str(3)
        tempInp[:] = inp[:]
    elif reflection(tempInp) == op:
        ans = str(4)
    elif rotate(tempInp) == op:
        ans = str(5)
    else:
        ans = str(7)
    fout.write(ans + "\n")
    fout.close()
