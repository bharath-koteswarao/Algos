from collections import Counter as c

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        inp = input().strip().split()
        co = c(inp)
        valid = True
        if len(co) == 2:
            for i in co:
                if co[i] != 2:
                    valid = False
        elif len(co) == 1:
            for i in co:
                if co[i] != 4:
                    valid = False
        else:
            valid = False
        print("YES" if valid else "NO")
