"""
10100101111011111111
00000000000000000000
01011101110110101111
"""
if __name__ == '__main__':
    inp = []
    while True:
        l = input().strip()
        if l:
            inp.append(l)
        else:
            break
    for line in inp:
        l = line[10:]
        a = 0
        b = 0
        ans, index = 0, 0
        for i in range(0, len(l) - 2, 2):
            if l[i] == '1':
                a += 1
            if l[i + 1] == '1':
                b += 1
            if a > b:
                ans = "a"
                index = i
                break
            elif b > a:
                ans = "b"
                index = i
                break
        if ans == 0:
            print("TIE")
        elif ans == 'a':
            print("TEAM-A", 12 + index)
        elif ans == 'b':
            print("TEAM-B", 12 + index)
