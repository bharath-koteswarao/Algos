if __name__ == '__main__':
    l = []
    for _ in range(int(input().strip())):
        l.append(input().strip().split())
    l = sorted(l, key=lambda x: (int(x[2]) - int(x[1])), reverse=True)
    print(l[0][0], int(l[0][2]) - int(l[0][1]))
