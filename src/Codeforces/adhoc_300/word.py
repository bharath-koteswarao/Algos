if __name__ == '__main__':
    inp = input().strip()
    u, l = 0, 0
    for x in inp:
        if x.isupper():
            u += 1
        else:
            l += 1
    print(inp.upper() if u > l else inp.lower())
