if __name__ == '__main__':
    s, n = [int(__) for __ in input().strip().split()]
    lis = []
    for _ in range(n):
        a, b = [int(__) for __ in input().strip().split()]
        lis.append((a, b))
    lis.sort(key=lambda x: (x[0], x[1]))
    for drag in lis:
        if drag[0] >= s:
            print("NO")
            exit(0)
        else:
            s += drag[1]
    print("YES")
