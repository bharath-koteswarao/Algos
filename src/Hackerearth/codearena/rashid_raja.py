if __name__ == '__main__':
    st = input().strip()
    dic1, dic2 = {}, {}
    count = 0
    for i in range(len(st)):
        if st[i] not in dic1:
            dic1[st[i]] = i
            dic2[count] = st[i]
            count += 1
    for i in dic2:
        print(dic2[i], end="")
