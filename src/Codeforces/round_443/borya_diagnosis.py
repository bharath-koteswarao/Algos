if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    for i in range(n):
        a, b = [int(i) for i in input().strip().split(" ")]
        while a in dic:
            a += b
        dic[a] = 1
    print(dic)