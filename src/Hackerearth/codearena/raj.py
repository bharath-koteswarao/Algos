def pal(st):
    i, j = 0, len(st) - 1
    while i <= j:
        if st[i] == st[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    st = input().strip()
    dic = {}
    for i in range(len(st)):
        if st[i] in dic:
            dic[st[i]].append(i)
        else:
            dic[st[i]] = [i]
    count = 0
    for i in dic:
        lis = dic[i]
        for p in range(len(lis)):
            for q in range(p + 1, len(lis)):
                temp = st[lis[p]:lis[q] + 1]
                if pal(temp):
                    count += 1
    print(count + len(st))
