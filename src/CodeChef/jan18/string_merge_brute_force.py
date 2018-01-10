"""
1
4 4
abab
baba
"""


def divide(s1, s2, div, l):
    if s1 == "":
        # print(div + s2)
        l.append(div + s2)
    elif s2 == "":
        # print(div + s1)
        l.append(div + s1)
    else:
        divide(s1[1:], s2, div + s1[0], l)
        divide(s1, s2[1:], div + s2[0], l)


def cost(st):
    c = 0
    for j in range(len(st) - 1):
        if st[j] != st[j + 1]:
            c += 1
    c += 1
    return c


if __name__ == '__main__':
    l = []
    for _ in range(int(input().strip())):
        n, m = [int(i) for i in input().strip().split()]
        s1 = input().strip()
        s2 = input().strip()
        divide(s1, s2, "", l)
        l = list(set(l))
        mi, mis = 1000, ""
        for i in l:
            c = cost(i)
            if c < mi:
                mi = c
                mis = i
        print(mis, mi)
