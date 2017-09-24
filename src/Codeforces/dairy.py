if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        inp = input()
        if inp in l:
            print("YES")
        else:
            print("NO")
        l.append(inp)
