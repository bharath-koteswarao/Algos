from itertools import groupby

if __name__ == '__main__':
    inp = input().strip()
    f = False
    for x in groupby(inp):
        if len(list(x[1])) >= 7:
            f = True
            break
    print("YES" if f else "NO")
