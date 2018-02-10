if __name__ == '__main__':
    cost = 500
    five,ten,fifteen,twenty = [int(i) for i in input().strip().split()]
    req = 0
    req += (five // 4) * cost
    five %= 4
    req += (ten // 2) * cost
    ten %= 2
    req += twenty * cost
    req += (fifteen // 4) * 3 * cost
    fifteen %= 4
    l = []
    while fifteen > 0:
        l.append(15)
    while five > 0:
        l.append(5)
    while ten > 0:
        l.append(10)
    