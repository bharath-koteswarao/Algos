if __name__ == '__main__':
    n, m = [int(i) for i in input().strip().split(" ")]
    dic = {}
    for i in range(n):
        person, cost = [int(i) for i in input().strip().split(" ")]
        if person in dic:
            dic[person] += cost
        else:
            dic[person] = cost
    total = sum(dic.values())
    whole = int(total / m)
    equity = total - (whole * m)
    anita = whole + equity
    for i in dic:
        if i == 1:
            dic[i] = (dic[i] - anita)
        else:
            dic[i] = (dic[i] - whole)
    for i in dic:
        print(i, dic[i])
