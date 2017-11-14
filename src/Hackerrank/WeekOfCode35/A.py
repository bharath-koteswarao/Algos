if __name__ == '__main__':
    n = int(input().strip())
    mi = 10 ** 10
    ans = ""
    for _ in range(n):
        na, p = input().strip().split(" ")
        se = p.count('7')
        fo = p.count('4')
        if (se == fo) and se > 0 and se + fo == len(p):
            if int(p) < mi:
                ans = na
    print(ans if ans != "" else -1)
