if __name__ == '__main__':
    s = input().strip()[1:-1].split(", ")
    s = list(set(s))
    if len(s) == 1 and s[0] == '':
        print(0)
    else:
        print(len(s))
