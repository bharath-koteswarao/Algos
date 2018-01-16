def find(a, b, ans):
    if len(a) > 0:
        for i in range(len(a)):
            test = int(ans + a[i] + ''.join(sorted(a[:i] + a[i + 1:])))
            if test <= b:
                return find(a[:i] + a[i + 1:], b, ans + a[i])
    else:
        return ans


if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    if a == b:
        print(a)
    else:
        a = list(str(a))
        if len(str(b)) > len(str(a)):
            ans = ""
            for i in sorted(a)[::-1]:
                ans += str(i)
            print(ans)
        else:
            found = False
            a.sort(reverse=True)
            ans = find(a, b, "")
            print(ans)
