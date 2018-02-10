if __name__ == '__main__':
    n = int(input().strip())
    l = []
    for _ in range(n):
        temp = ['0' for i in range(10)]
        st = input().strip()
        for i in st:
            temp[int(i)] = '1'
        l.append(''.join(temp))
    dic = {}
    for i in l:
        for j in range(1, len(i) + 1):
            x = int(i[-1 * j:], 2)
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
    ans = 0
    for i in l:
        req = int(i, 2)
        if req in dic:
            print(dic[req])
