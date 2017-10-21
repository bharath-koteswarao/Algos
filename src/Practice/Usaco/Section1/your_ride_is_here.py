"""
ID: koteswa1
LANG: PYTHON3
PROG: ride
"""


def num(char):
    return ord(char) - ord('A') + 1


def prod(string):
    mul = 1
    for i in string:
        mul *= num(i)
    return mul


if __name__ == '__main__':
    fin = open('ride.in', 'r')
    fout = open('ride.out', 'w')
    comet = fin.readline()
    group = fin.readline()
    comet = prod(comet)
    group = prod(group)
    print(comet, group)
    ans = "GO" if comet % 47 == group % 47 else "STAY"
    fout.write(ans + "\n")
    fout.close()
