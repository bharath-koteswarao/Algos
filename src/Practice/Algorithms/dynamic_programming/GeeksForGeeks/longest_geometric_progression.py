"""
6
5 7 15 10 20 29
"""
if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        input()
        inp = [int(i) for i in input().strip().split(" ")]
        l = []
        for i in range(len(inp)):
            for j in range(i + 1, len(inp)):
                if inp[j] % inp[i] == 0:
                    l.append([inp[i], inp[j]])
        dic = {}
        for i in inp:
            dic[i] = 1
        while True:
            count = 0
            for lis in l:
                out = lis[-1]
                ratio = lis[-1] // lis[-2]
                if out * ratio in dic:
                    lis.append(out * ratio)
                else:
                    count += 1
            if count == len(l):
                break
        ans = 0
        for i in l:
            ans = max(ans, len(i))
        print(ans)
