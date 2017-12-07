if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n = int(input().strip())
        arr = [int(i) for i in input().strip().split(" ")]
        dic = {}
        for i in arr:
            if i % 10 in dic:
                dic[i%10] += 1
            else:
                dic[i%10] = 0
        s = 0
        for i in dic:
            s += dic[i]
        print(s)
