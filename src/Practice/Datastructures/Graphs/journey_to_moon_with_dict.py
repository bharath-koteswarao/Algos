def c(n, r):
    if n == 0:
        return 0
    elif n == r:
        return 1
    elif r > n:
        return 0
    else:
        return (n * (n - 1)) // 2


if __name__ == '__main__':
    n, p = [int(i) for i in input().strip().split(" ")]
    dic = {}
    last_key = 0
    for i in range(p):
        i1, i2 = [int(j) for j in input().strip().split(" ")]
        if i1 not in dic and i2 not in dic:
            dic[i1] = last_key
            dic[i2] = last_key
            last_key += 1
        elif i1 in dic and i2 not in dic:
            dic[i2] = dic[i1]
        elif i1 not in dic and i2 in dic:
            dic[i1] = dic[i2]
        elif i1 in dic and i2 in dic:
            pass
    for i in range(n):
        if i not in dic:
            dic[i] = last_key
            last_key += 1
    print(dic)
    count = {}
    for i in range(last_key):
        count[i] = 0
    for i in dic:
        count[dic[i]] += 1
    print(count)
    # remove = 0
    # total = (n * (n - 1)) // 2
    # for i in count:
    #     remove += c(count[i], 2)
    # print(total - remove)
