def get(i, l, ans):
    if i != len(s):
        if s[i] == '0':
            get(i + 1, l, ans + '1')
            get(i + 1, l, ans + '0')
        else:
            get(i + 1, l, ans + '1')
    else:
        l.append(ans)


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    for _ in range(int(input().strip())):
        x,y = [int(i) for i in input().strip().split()]
