"""
ID: koteswa1
LANG: PYTHON3
PROG: milk
"""

if __name__ == '__main__':
    fin = open('milk.in', 'r')
    fout = open('milk.out', 'w')
    n, f = [int(i) for i in fin.readline().strip().split()]
    l = []
    for _ in range(f):
        a, b = [int(i) for i in fin.readline().strip().split()]
        l.append((a, b))
    l.sort(key=lambda x: (x[0], x[1]))
    req, cost = 0, 0
    for i in range(len(l)):
        if req + l[i][1] <= n:
            req += l[i][1]
            cost += l[i][0] * l[i][1]
        else:
            cost += l[i][0] * (n - req)
            break
    ans = str(cost)
    fout.write(ans + "\n")
    fout.close()
