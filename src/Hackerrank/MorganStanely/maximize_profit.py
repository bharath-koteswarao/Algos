if __name__ == '__main__':
    n, b, c = [int(i) for i in input().strip().split(" ")]
    i1 = [int(i) for i in input().strip().split(" ")]
    i2 = [int(i) for i in input().strip().split(" ")]
    l = [b * c]
    for i in range(n):
        l.append(b * i1[i] * i2[i])
    print(max(l))
