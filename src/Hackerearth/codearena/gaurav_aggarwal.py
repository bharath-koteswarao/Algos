if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n = int(input().strip())
        a = "The streak lives still in our heart!"
        b = "The streak is broken!"
        s1 = str(n)
        found = False
        for i in range(len(s1)):
            for j in range(i + 1, len(s1)):
                if s1[i] == '2' and s1[j] == '1':
                    found = True
                if found:
                    break
            if found:
                break
        if found:
            print(b)
        elif n % 21 == 0:
            print(b)
        else:
            print(a)
