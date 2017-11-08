if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n, r = [int(i) for i in input().strip().split(" ")]
        inp = [int(i) for i in input().strip().split(" ")]
        s = sorted(inp)
        dic = {}
        for i, j in enumerate(s):
            dic[j] = i
        bounds = [0, n - 1]
        if n > 1:
            stop = False
            for i in range(0, n - 1):
                if inp[i + 1] > inp[i]:
                    di = "right"
                else:
                    di = "left"
                if bounds[0] <= dic[inp[i]] <= bounds[1]:
                    if di == "left":
                        bounds[1] = min(bounds[1], dic[inp[i]])
                    else:
                        bounds[0] = max(bounds[0], dic[inp[i]])
                else:
                    stop = True
                if stop:
                    break
            print("YES" if not stop else "NO")
        else:
            print("YES")
