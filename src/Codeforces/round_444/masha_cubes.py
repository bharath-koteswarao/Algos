if __name__ == '__main__':
    n = int(input().strip())
    arrs = [[] for i in range(n)]
    for _ in range(n):
        arrs[_] = [int(i) for i in input().strip().split(" ")]
    h = []
    for i in arrs:
        h.append((max(i)))
    dic = {}
    for i in range(n):
        for j in arrs[i]:
            if j in dic:
                dic[j].append(i + 1)
            else:
                dic[j] = [i + 1]
    highest = int("".join([str(i) for i in sorted(h)][::-1]))
    answer = 0
    stop = False
    for i in range(1, highest + 1):
        temp = set()
        lis = list(str(i))
        for j in lis:
            if int(j) not in dic:
                stop = True
            else:
                temp = temp.union(set(dic[int(j)]))
            if stop:
                break
        if len(temp) >= len(str(i)) and not stop:
            answer = i
        else:
            stop = True
        if stop:
            break
    print(answer)
