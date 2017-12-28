"""
ID: koteswa1
LANG: PYTHON3
PROG: milk2
"""
if __name__ == '__main__':
    fin = open('milk2.in', 'r')
    fout = open('milk2.out', 'w')
    n = int(fin.readline())
    l = []
    for _ in range(n):
        a, b = [int(i) for i in fin.readline().strip().split()]
        l.append((a, b))
    l.sort(key=lambda p: (p[0], p[1]))
    first, last = l[0]
    ma, nma = last - first, 0
    for i in range(1, len(l)):
        x, y = l[i]
        if x <= last:
            last = y if y > last else last
            ma = max(ma, last - first)
        else:
            nma = max(nma, x - last)
            first, last = x, y
    ans = str(ma) + " " + str(nma)
    fout.write(ans + "\n")
    fout.close()
