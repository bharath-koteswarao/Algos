if __name__ == '__main__':
    st = input().strip()
    s = "hello"
    i, j = 0, 0
    while i < len(st) and j < len(s):
        if st[i] == s[j]:
            j += 1
        i += 1
    print("YES" if j == len(s) else "NO")
