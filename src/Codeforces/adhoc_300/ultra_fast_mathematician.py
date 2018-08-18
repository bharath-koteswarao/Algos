if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += '0'
        else:
            ans += '1'
    print(ans)
