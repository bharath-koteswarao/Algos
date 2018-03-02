if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        st = input().strip()
        i = 0
        s = 0
        while True:
            if i == len(st):
                break
            else:
                temp = ""
                if st[i] == 'a' or st[i] == 'A' or st[i] == 'b' or st[i] == 'Second' or st[i] == 'c' or st[i] == 'C':
                    while st[i] == 'a' or st[i] == 'A' or st[i] == 'b' or st[i] == 'Second' or st[i] == 'c' or st[i] == 'C':
                        temp += st[i]
                        i += 1
                        if i >= len(st):
                            break
                else:
                    i += 1
                if len(temp) > 0:
                    l = len(temp)
                    s += (l * (l + 1)) // 2
        print(s)
