from collections import Counter

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        inp = input().strip()
        if len(inp) == 2:
            print("1 2" if inp[0] == inp[1] else "-1")
        else:
            c = Counter(inp)
            count = 0
            for i in c:
                if c[i] % 2 == 1:
                    count += 1
            if len(inp) % 2 == 1:
                if count != 1:
                    print(-1)
                else:
                    cen = 0
                    l1, l2 = [], []
                    dic = {}
                    for i in range(len(inp)):
                        if inp[i] in dic:
                            dic[inp[i]].append(i + 1)
                        else:
                            dic[inp[i]] = [i + 1]
                    for i in dic:
                        x = dic[i]
                        if c[i] % 2 == 0:
                            for j in range(len(x)):
                                if j % 2 == 0:
                                    l1.append(x[j])
                                else:
                                    l2.append(x[j])
                        else:
                            cen = dic[i]
                    ans = ""
                    for i in l1:
                        ans += str(i) + " "
                    for i in cen:
                        ans += str(i) + " "
                    for i in l2[::-1]:
                        ans += str(i) + " "
                    print(ans)
            else:
                if count != 0:
                    print(-1)
                else:
                    dic = {}
                    for i in range(len(inp)):
                        if inp[i] in dic:
                            dic[inp[i]].append(i + 1)
                        else:
                            dic[inp[i]] = [i + 1]
                    l1, l2 = [], []
                    for i in dic:
                        x = dic[i]
                        for j in range(len(x)):
                            if j % 2 == 0:
                                l1.append(x[j])
                            else:
                                l2.append(x[j])
                    ans = ""
                    for i in l1:
                        ans += str(i) + " "
                    for i in l2[::-1]:
                        ans += str(i) + " "
                    print(ans)
