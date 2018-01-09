def print_answer(x, l1):
    ans = [0] * n
    ans[x - 1] = 2
    for i in l1:
        ans[i - 1] = 1
    s = ""
    for i in ans:
        s += str(i)
    print(s)


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        x, n = [int(i) for i in input().strip().split()]
        tot = (n * (n + 1)) // 2
        if (tot - x) % 2 != 0 or n <= 3:
            print("impossible")
        else:
            l1, l2 = [], []
            dic1, dic2 = {}, {}
            s1, s2 = 0, 0
            for i in range(n, 0, -1):
                if i != x:
                    if s1 < s2:
                        s1 += i
                        l1.append(i)
                        dic1[i] = 0
                    else:
                        s2 += i
                        l2.append(i)
                        dic2[i] = 0
            # print(s1, s2)
            # print(l1)
            # print(l2)
            if s1 == s2:
                print_answer(x, l1)
            else:
                l1.sort()
                l2.sort()
                el = 0
                if s1 < s2:
                    for i in l1:
                        if i + 1 in l2:
                            el = i
                            break
                    l1.remove(el)
                    l1.append(el + 1)
                    print_answer(x, l1)
                else:
                    for i in l2:
                        if i + 1 in l1:
                            el = i
                            break
                        l2.remove(el)
                        l2.append(el + 1)
                        print_answer(x, l2)
