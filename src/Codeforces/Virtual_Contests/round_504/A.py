if __name__ == '__main__':
    input()
    s1 = input().strip()
    s2 = input().strip()
    if '*' not in s1:
        print("YES" if s1 == s2 else "NO")
    elif s1 == '*':
        print("YES")
    elif s1[-1] == '*':
        print("YES" if s2.startswith(s1[:-1]) else "NO")
    else:
        s1 = s1.split('*')
        if s2.startswith(s1[0]):
            s2 = s2[len(s1[0]):]
            print("YES" if s2.endswith(s1[1]) else "NO")
        else:
            print("NO")
