from collections import Counter as c

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        s1 = input().strip()
        s2 = input().strip()
        c1 = c(s1)
        c2 = c(s2)
        valid = True
        for i in c1:
            if i not in c2:
                valid = False
                break
        if not valid:
            print(-1)
        else:
            ans = {}
            for i in range(len(s2) - len(s1) + 1):
                co = c1.copy()
                for j in range(i, i + len(s1)):
                    if s2[j] in co:
                        co[s2[j]] -= 1
                    else:
                        break
                    if co[s2[j]] == 0:
                        del co[s2[j]]
                if len(co) == 0:
                    st = s2[i:i + len(s1)]
                    if st in ans:
                        ans[st] += 1
                    else:
                        ans[st] = 1
            if len(ans) == 0:
                print(-1)
            else:
                mk = 0
                for i in ans:
                    mk = max(mk, ans[i])
                li = []
                for i in ans:
                    if ans[i] == mk:
                        li.append(i)
                li.sort()
                print(li[0])
