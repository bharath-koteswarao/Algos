x = int(input())
h, m = map(int, input().split(' '))

cnt = 0


def chk(h, m):
    i = "7"
    if i in str(h) or i in str(m):
        return 0
    else:
        return 1


fg = chk(h, m)
while fg:
    if m > x:
        m -= x
    elif h > 0:
        h -= 1
        temp = m - x
        m = 60 + temp
    else:
        h = 23
        temp = m - x
        m = 60 + temp
    cnt += 1
    fg = chk(h, m)
print(cnt)
