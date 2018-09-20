from collections import Counter

if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    co = Counter(arr)
    count = 0
    gt2 = 0
    for x in co:
        if co[x] == 1:
            count += 1
        elif co[x] > 2:
            gt2 += 1
    if count % 2 != 0 and gt2 == 0:
        print("NO")
    else:
        req = False
        if count % 2 != 0:
            req = True
        print("YES")
        ans = ['0' for i in range(len(arr))]
        idx = {}
        for i in range(len(arr)):
            if arr[i] in idx:
                idx[arr[i]].append(i)
            else:
                idx[arr[i]] = [i]
        last = True
        for i in range(len(arr)):
            if co[arr[i]] == 1:
                ans[i] = 'A' if last else 'B'
                last = not last
            elif co[arr[i]] == 2:
                ans[idx[arr[i]][0]] = 'A'
                ans[idx[arr[i]][1]] = 'B'
            else:
                done = False
                if not req:
                    ans[i] = 'A'
                else:
                    if done:
                        ans[i] = 'A'
                    else:
                        done = True
                        if ans.count('A') > ans.count('B'):
                            ans[idx[arr[i]][0]] = 'B'
                            for ii in range(1, len(idx[arr[i]])):
                                ans[idx[arr[i]][0]] = 'A'
                        else:
                            ans[idx[arr[i]][0]] = 'A'
                            for ii in range(1, len(idx[arr[i]])):
                                ans[idx[arr[i]][0]] = 'B'

        print(''.join(ans))
        l1, l2 = [], []
        for i in range(len(arr)):
            if ans[i] == 'A':
                l1.append(arr[i])
            else:
                l2.append(arr[i])
        print(l1, l2)
