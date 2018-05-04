from math import gcd as gc


def get(l):
    g = l[0]
    for i in range(1, len(l)):
        g = gc(g, l[i])
    return g


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        input()
        l = [int(__) for __ in input().strip().split()]
        gcd = get(l)
        print(0 if gcd == 1 else -1)
