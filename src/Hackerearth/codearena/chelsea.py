if __name__ == '__main__':
    dic = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        6: 6,
        7: 3,
        8: 7,
        9: 6,
        5: 5,
    }
    s = 0
    l = [int(i) for i in list(input().strip())]
    for i in l:
        s += dic[i]
    print(s)
