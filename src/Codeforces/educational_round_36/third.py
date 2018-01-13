if __name__ == '__main__':
    a = [int(i) for i in list(input().strip())]
    b = [int(i) for i in list(input().strip())]
    if len(b) > len(a):
        a.sort(reverse=True)
        ans = ""
        for i in a:
            ans += str(i)
        print(ans)
    else:
        a.sort(reverse=True)
        j,k = 0,0
        ans = ""
        while True:
            if a[j] == b[k]:
                pass
