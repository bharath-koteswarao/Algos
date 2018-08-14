def isVowel(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or ch == 'y' or ch == 'Y':
        return True
    else:
        return False


if __name__ == '__main__':
    inp = input().strip()
    ans = ""
    for i in inp:
        if not isVowel(i):
            ans += '.'
            ans += i.lower()
    print(ans)
