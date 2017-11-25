if __name__ == '__main__':
    input()
    inp = [int(i) for i in input().strip().split(" ")]
    d = {}
    for i in range(len(inp)):
        d[inp[i]] = i + 1
    for i in sorted(d):
        print(d[d[i]])
