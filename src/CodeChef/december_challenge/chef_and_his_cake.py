"""
Input:

2
4 5
RGRGR
GRGRG
RGRGR
GRGRG
2 3
RRG
GGR

Output:

0
8

"""
if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n, m = [int(i) for i in input().strip().split(" ")]
        x = [0] * n
        for i in range(n):
            x[i] = list(input().strip())
        f = [[0 for i in range(m)] for j in range(n)]
        s = [[0 for i in range(m)] for j in range(n)]
        for i in range(len(f)):
            for j in range(len(f[i])):
                f[i][j] = ('R' if (i + j) % 2 == 0 else 'G')
                s[i][j] = ('G' if (i + j) % 2 == 0 else 'R')
        c1, c2 = 0, 0
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j] == 'R':
                    if 'R' != f[i][j]:
                        c1 += 5
                    if 'R' != s[i][j]:
                        c2 += 5
                else:
                    if 'G' != f[i][j]:
                        c1 += 3
                    if 'G' != s[i][j]:
                        c2 += 3
        print(min(c2, c1))
