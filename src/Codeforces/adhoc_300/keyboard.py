if __name__ == '__main__':
    ch = input().strip()
    s = "qwertyuiopasdfghjkl;zxcvbnm,./"
    inp = input().strip()
    for x in inp:
        print(s[s.index(x) - 1] if ch == "R" else s[s.index(x) + 1], end="")
