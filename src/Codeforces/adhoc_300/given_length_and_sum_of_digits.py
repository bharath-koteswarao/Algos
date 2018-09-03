if __name__ == '__main__':
    m, s = [int(__) for __ in input().strip().split()]
    big, small = "", ""

    # big
    if s == 0:
        if m > 1:
            big = "-1"
        else:
            big = "0"
    else:
        sc = s * 1
        if s > 9 * m:
            big = '-1'
        else:
            while sc > 0:
                if sc >= 9:
                    big += '9'
                    sc -= 9
                else:
                    big += str(sc)
                    sc = 0
        if len(big) != m and big != "-1":
            big += '0' * (m - len(big))
    # small
    if s == 0:
        if m > 1:
            small = "-1"
        else:
            small = "0"
    elif s > 9 * m:
        small = "-1"
    else:
        sl = [1]
        s -= 1
        for i in range(m - 1):
            sl.append(0)
        for i in range(m - 1, -1, -1):
            if s <= 0:
                break
            else:
                if s >= 9:
                    sl[i] = 9
                    s -= 9
                else:
                    sl[i] += s
                    s = 0
        small = ''.join([str(x) for x in sl])
    print(small, big)
