if __name__ == '__main__':
    n = int(input().strip())
    l = []
    for i in range(n):
        l.append([int(__) for __ in input().strip().split()])
    l.sort(key=lambda x: (x[0], x[1]))
    inte = l[0]
    print(l)
