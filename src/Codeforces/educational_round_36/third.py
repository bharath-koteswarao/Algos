if __name__ == '__main__':
    a = list(input().strip())
    b = int(input().strip())
    if len(str(b)) > len(str(a)):
        ans = ""
        for i in sorted(a)[::-1]:
            ans += str(i)
        print(ans)
    else:
        ans = ""
        a.sort(reverse=True)
        while len(a) > 0:
            for i in range(len(a)):
                if int(a[i] + ''.join(a[i + 1:][::-1] + a[:i][::-1])) < b:
                    ans += str(a[i])
        print(ans)
